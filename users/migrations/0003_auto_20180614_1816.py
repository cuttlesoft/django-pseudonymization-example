# Generated by Django 2.0.6 on 2018-06-14 18:16

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180611_1937'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]