from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    Mobile_no = models.CharField(max_length=10, primary_key=True)

    class Types(models.TextChoices):
        Farmer = "FARMER"
        Customer = "CUSTOMER"
        Seller = "SELLER"

    type = models.CharField(max_length=50, choices=Types.choices, default=Types.Farmer)
    address = models.TextField(max_length=255, default="none", null=True)
    city = models.TextField(max_length=50, default="none", null=True)
    state = models.TextField(max_length=50, default="none", null=True)
    zipcode = models.TextField(max_length=10, default="none", null=True)
    uname = models.TextField(max_length=255, default="none", null=True)
    email = models.TextField(max_length=100, default="none", null=True)
    profile_pic = models.ImageField(upload_to="user/profilepics", default="static/images/profile_pic.jpg", null=True)
    update_on = models.DateTimeField(auto_now=True)


