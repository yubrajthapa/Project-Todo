# Generated by Django 4.0.6 on 2022-07-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0003_remove_userdetails_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='is_verified',
            field=models.BooleanField(null=True),
        ),
    ]
