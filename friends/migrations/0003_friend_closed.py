# Generated by Django 3.2.13 on 2022-11-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_friend_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]