# Generated by Django 2.2.16 on 2020-10-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0004_auto_20201031_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_climate',
            name='humidity',
            field=models.FloatField(blank=True, null=True, verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='room_climate',
            name='temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Temperature'),
        ),
    ]