from django.db import models
from crop.models  import *

# Create your models here.
class add_MarketPrice(models.Model):
    userid = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET)
    Product = models.ForeignKey(crop, null=True, on_delete=models.SET)
    Price = models.IntegerField(default=0)
    Yard_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Yard_name