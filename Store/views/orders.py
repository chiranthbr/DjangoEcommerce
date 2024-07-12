from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from Store.models.customer import Customer
from django.views import View
from Store.models.products import Products
from Store.models.orders import Orders
# from Store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Orders.getOrdersByCustomer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})