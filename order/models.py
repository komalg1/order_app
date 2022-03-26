from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# # Create your models here.

##Customer model - Basic data of the customers
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.user)

##Order details of the customer
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(default=now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([1 for item in orderitems])
        return total

##Data of an individual product
class Product(models.Model):
   name = models.CharField(max_length=100)
   price = models.FloatField()
   quantity_in_stock = models.IntegerField(default=0)

   def __str__(self):
       return self.name
    

##Combination of the Product & the Order ordered by the Customer
class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name