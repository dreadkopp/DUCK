# Generated by Django 2.2.3 on 2019-07-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duckchat', '0003_auto_20190716_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatuser',
            name='icon',
            field=models.ImageField(default='user_icons/no-img.png', upload_to='user_icons/'),
        ),
    ]
