from django.db import models

# Create your models here.

class Category_Machine(models.Model):
    cname = models.CharField(max_length=20)

    def __str__(self):
        return self.cname

    @staticmethod
    def get_all_category():
        return Category_Machine.objects.all()

    def get_name_by_catid(category_id):
        if category_id:
            return Category_Machine.objects.get(id=category_id)
        else:
            pass


class machine(models.Model):
    userid = models.IntegerField(default=0)
    category = models.ForeignKey(Category_Machine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Description = models.CharField(max_length=5000)
    key_players = models.CharField(max_length=200)
    Approx_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to="buy_machine/images", default="", null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return machine.objects.all()

    @staticmethod
    def get_all_products_by_catid(category_id):
        if category_id:
            return machine.objects.filter(category=category_id)
        else:
            return machine.get_all_products()


class Order_machine(models.Model):
    userid = models.IntegerField(default=0)
    order_id = models.AutoField(primary_key=True)
    item_json = models.JSONField()
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=10, default=" ")
    order_date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=50, default="")
    paid = models.BooleanField(default=False)
