# Generated by Django 2.2.16 on 2020-10-31 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=200, verbose_name='Room')),
                ('temperature', models.FloatField(verbose_name='Temperature')),
                ('humidity', models.FloatField(verbose_name='Humidity')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Time')),
            ],
        ),
    ]
