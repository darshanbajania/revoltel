# Generated by Django 3.1.2 on 2020-11-23 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revoltel_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='api_integration',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='batt_included',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='batt_required',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='codec',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='manufacturer',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='model_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='supportive_channels',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='warrenty',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase_details',
            name='time_of_purchase',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 23, 10, 25, 54, 457029)),
        ),
    ]
