from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from datetime import datetime, timedelta
from duckchat.models import ChatRoom, Message
from duckchat.services.UserService import UserService


def landingpage(request, room_id=None, passwd=None):
    template = loader.get_template("Main.html")
    if not room_id:
        room_id = 1
    chatroom = ChatRoom.objects.get(pk=room_id)
    if chatroom.type == 2:  # 2 is Private
        if passwd != chatroom.password:
            return HttpResponse('Du brauchst das korrekte Passwort, um diesem Chatroom beizutreten')
    hour_ago = datetime.now() - timedelta(hours=1)
    messages = Message.objects.filter(room=room_id)
    lastMessage = messages.last()
    messages = messages.filter(timestamp__gt=hour_ago)
    lastMessageID = 0
    if lastMessage:
        lastMessageID = lastMessage.id
    users = UserService.get_current_users()
    available_rooms = ChatRoom.objects.all()

    context = {
        'room': chatroom,
        'messages': messages,
        'users': users,
        'available_rooms': available_rooms,
        'password': passwd,
        'lastMessageID': lastMessageID
    }
    returndata = template.render(context, request)
    return HttpResponse(returndata)

def getMessages(request):
    # check if request is send as POST
    if request.method != 'GET':
        return HttpResponse('Kann Nachrichten nur per GET empfangen')
    room_id = request.GET.get('room_id',1)
    passwd = request.GET.get('passwd','')
    user = request.user
    lastmessageID = request.GET.get('lastmessageID',1)

    chatroom = ChatRoom.objects.get(pk=room_id)
    if chatroom.type == 2:  # 2 is Private
        if passwd != chatroom.password:
            return HttpResponse('Du brauchst das korrekte Passwort, um diesem Chatroom beizutreten')
    messages = Message.objects.filter(room=room_id).filter(pk__gt=lastmessageID)
    prettymessages = []
    for message in messages:
        prettymessage = prettifyMessages(message.sender, message)
        prettymessages.append(prettymessage)

    return JsonResponse(prettymessages, safe=False)


def acceptMessage(request):
    # check if request is send as POST
    if request.method != 'POST':
        return HttpResponse('Kann Nachrichten nur per Post empfangen')

    # create new Message and store it to DB
    message = Message()
    message.sender = request.user
    message.message = request.POST.get('Message')
    room_id = request.POST.get('roomid')
    message.room = ChatRoom.objects.get(pk=room_id)
    message.save()

    # get some user info for display
    name = request.user.nickname
    if not name:
        name = request.user.username
    image = request.user.icon
    if not image:
        image = 'user_icons/no-img.png'
    else:
        image = image.url

    data = []
    lastID = request.POST.get('lastmessageID', 1)
    messages = Message.objects.filter(room=room_id).filter(pk__gt=lastID)

    for message in messages:
        prettymessage = prettifyMessages(message.sender, message)
        data.append(prettymessage)

    # data = prettifyMessages(request.user, message)

    return JsonResponse(data, safe=False)


def prettifyMessages(user, message):
    name = user.nickname
    if not name:
        name = user.username
    image = user.icon
    if not image:
        image = 'user_icons/no-img.png'
    else:
        image = image.url
    return {'message': model_to_dict(message),
             'sender': name,
             'sender_image': image,
             'time': message.timestamp.strftime("%d.%m %H:%M"),
             'user_id': user.id
             }