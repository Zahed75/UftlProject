from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderFuel(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    company_name = models.CharField(max_length=200, blank=False)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(max_length=220, blank=True)
    message = models.TextField(max_length=4000, blank=True)
    fuel_type = models.CharField(max_length=220, blank=False)  # drop Down
    order_area = models.CharField(max_length=220, blank=False)
    fuel_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.full_name


class fuel_utils(models.Model):
    fuel_type = models.CharField(max_length=220, blank=False)  # drop Down
    order_area = models.CharField(max_length=220, blank=False)  # drop down
    
    def __str__(self):
        return self.fuel_type
