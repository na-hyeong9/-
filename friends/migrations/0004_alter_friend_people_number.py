# Generated by Django 3.2.13 on 2022-11-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_friend_people_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='people_number',
            field=models.IntegerField(),
        ),
    ]
