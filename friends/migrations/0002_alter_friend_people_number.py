# Generated by Django 3.2.16 on 2022-11-21 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='people_number',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
