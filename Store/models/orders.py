from django.db import models
from .products import Products
from .customer import Customer
import datetime

class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length=500, default = '', blank = True)
    phone = models.CharField(max_length = 10)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def getOrdersByCustomer(custId):
        return Orders.objects.filter(customer = custId). order_by('-date')