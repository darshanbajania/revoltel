# Generated by Django 3.1.2 on 2020-11-13 05:27

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=300)),
                ('product_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='avatar')),
                ('description', models.CharField(default='product description', max_length=1500)),
                ('price', models.CharField(default='100', max_length=20)),
                ('availability', models.CharField(default='No', max_length=10)),
                ('product_type', models.CharField(default='NO type', max_length=100)),
                ('stock', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(default='1', max_length=15)),
                ('customers_purchased_id', models.CharField(default='', max_length=10)),
                ('time_of_purchase', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 13, 10, 57, 19, 484715))),
                ('products_detail', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_user_id', models.CharField(default='user_id', max_length=15)),
                ('total_users', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(default='no_id', max_length=20)),
                ('full_name', models.CharField(default='user', max_length=100)),
                ('email_id', models.CharField(default='user.gmail.com', max_length=100)),
                ('address', models.CharField(default='address', max_length=500)),
                ('purchased_product_id', models.CharField(default='[]', max_length=500)),
                ('currently_purchased_products', models.CharField(default='{}', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
