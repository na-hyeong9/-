# Generated by Django 3.2.13 on 2022-11-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_hotel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
