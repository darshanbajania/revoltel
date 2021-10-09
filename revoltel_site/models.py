from django.db import models
from django.contrib.auth.models import User
import datetime 
from cloudinary.models import CloudinaryField
from django.utils.timezone import now

# Create your models here.
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    customer_id = models.CharField(default="no_id", max_length=20)
    full_name = models.CharField(default="user", max_length=100)
    email_id = models.CharField(default="user.gmail.com", max_length=100)
    address = models.CharField(default="address", max_length=500)
    purchased_product_id = models.CharField(default="[]", max_length=500)
    currently_purchased_products = models.CharField(default="{}", max_length=200)
    def __str__(self):
        return f'Customer:  {self.customer_id}'

    def save(self, *args, **kwargs):
        super().save()

class Products(models.Model):
    product_id = models.IntegerField(default="1000")
    product_name = models.CharField(max_length=300)
    product_image = CloudinaryField('avatar')
    description = models.CharField(default="product description", max_length=1500)
    price = models.CharField(default='100', max_length=20)
    brand = models.CharField(default="None", max_length=100)
    manufacturer = models.CharField(default="None", max_length=100)
    model_name = models.CharField(default="None", max_length=100)
    batt_included = models.CharField(default="No", max_length=100)
    batt_required = models.CharField(default = "No", max_length=100)
    codec = models.CharField(default = "None", max_length=100)
    supportive_channels = models.CharField(default = "None", max_length = 100)
    api_integration = models.CharField(default = "None", max_length = 100)
    warrenty = models.CharField(default = "None", max_length=100)
    availability = models.CharField(default="No", max_length=10)
    product_type = models.CharField(default="NO type", max_length=100)
    stock = models.IntegerField(default="0")


    def __str__(self):
        return f'{self.product_name}'


class User_id(models.Model):
    new_user_id = models.CharField(default="user_id",max_length=15)
    total_users = models.IntegerField(default="0")

    def __str__(self):
        return f'user_id_detail'

class Purchase_details(models.Model):
    purchase_id = models.CharField(default="1", max_length=15)
    customers_purchased_id = models.CharField(default="",max_length=10)
    time_of_purchase = models.DateTimeField(default=now, blank=True)
    products_detail = models.CharField(default="",max_length=100)

    def __str__(self):
        return f'{self.purchase_id}'


class Cutomers_temp_details(models.Model):
    cutomer_id =models.IntegerField(default = '00000')
    cutomer_name = models.CharField(default = 'No NAME', max_length=500)
    Customer_email_id  = models.CharField(default = 'No email_id', max_length= 200)
    customer_phone_number = models.IntegerField(default="9999999999")
    customer_cart_contents = models.CharField(default = "{}", max_length=500)

    def __str__(self):
        return f'{self.customer_id}'



