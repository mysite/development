# Generated by Django 2.2.16 on 2020-11-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0006_historicalperson_historicalpersonvehicle_person_personvehicle_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_climate',
            name='humidity',
            field=models.FloatField(blank=True, null=True, verbose_name='humidity'),
        ),
        migrations.AlterField(
            model_name='room_climate',
            name='room',
            field=models.CharField(max_length=200, verbose_name='room'),
        ),
        migrations.AlterField(
            model_name='room_climate',
            name='temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='temperature'),
        ),
        migrations.AlterField(
            model_name='room_climate',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time'),
        ),
    ]
