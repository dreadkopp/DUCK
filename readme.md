Setup:

1. create a virtualenvironment
  - python -m venv venv
  
2. start the venv
  - source ./venv/bin/activate
  
3. install needed packaged
  - pip install -r requirements.txt
  
4. create initial Databasestructure
  - ./manage.py migrate
    
5. provide initial dataset
  - ./manage.py loaddata fixtures/initialSeed.json
  
6. start the server with binding to available network interfaces
  - ./manage.py runserver 0.0.0.0:8000
  
7. login to the admin-interface, correct your admin data, add Chatrooms if you like
  - default login:password is admin:admin
  - admin-backend can be found at <ip_of_your_server>:8000/admin  