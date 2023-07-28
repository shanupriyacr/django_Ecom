from django.db import models

from shop.models import Product


from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cart(models.Model):
    DoesNotExist = None
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    active=models.BooleanField(default=True)
    def subtotal(self):
        return self.quantity * self.products.price

    def __str__(self):
        return self.products.name

# self.quantity= quantity of current object


# TABLE "accounts"  --> for getting payment and account details  (normally gateway will use)

class Account(models.Model):
    objects = None
    acctnumber=models.CharField(max_length=200)
    acctype=models.CharField(max_length=200)
    amount=models.IntegerField()

    def __str__(self):
        return self.acctnumber


# TABLE "order"  -->  for storing order details

class Order(models.Model):
    objects = None
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.TextField()
    phone= models.CharField(max_length=100)
    order_status=models.CharField(max_length=30,default="Pending")          # after payment status become "completed"
    delivery_status=models.CharField(max_length=30,default="Pending")       # after delivery status become "completed"
    noofitems=models.IntegerField()

    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    def subtotal(self):
        return self.noofitems * self.products.price

# auto_now_add=True -->capture and store the timestamp of when an object was created

