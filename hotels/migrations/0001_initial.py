# Generated by Django 3.2.13 on 2022-11-11 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.TextField()),
                ('rating', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('facilities', models.TextField()),
                ('image', models.TextField()),
                ('detail_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.detailregion')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.region')),
            ],
        ),
    ]