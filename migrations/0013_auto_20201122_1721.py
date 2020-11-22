# Generated by Django 3.1.2 on 2020-11-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0012_share_movement'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_movement',
            name='currency',
            field=models.CharField(choices=[('euro', 'Euro'), ('usd', 'USD')], default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='share_movement',
            name='exchange_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='exchange_rate'),
        ),
        migrations.AlterField(
            model_name='share_movement',
            name='cost',
            field=models.FloatField(blank=True, null=True, verbose_name='cost'),
        ),
        migrations.AlterField(
            model_name='share_movement',
            name='expenses',
            field=models.FloatField(blank=True, null=True, verbose_name='expenses'),
        ),
        migrations.AlterField(
            model_name='share_movement',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='quantity'),
        ),
    ]
