# Generated by Django 3.1.2 on 2020-11-23 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revoltel_site', '0002_auto_20201123_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_details',
            name='time_of_purchase',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 23, 17, 30, 48, 863100)),
        ),
    ]
