# Generated by Django 4.0.6 on 2022-07-22 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_userdetails_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='is_verified',
        ),
    ]