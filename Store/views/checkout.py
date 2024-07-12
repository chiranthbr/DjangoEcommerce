from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from Store.models.customer import Customer
from django.views import View

from Store.models.products import Products
from Store.models.orders import Orders

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = request.getProductsById(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Orders(customer = Customer(id = customer),
                           product = product,
                           price = product.price,
                           address = address,
                           quantity = cart.get(str(product.id)),
                           phone = phone)
            order.save()

        request.session['cart'] = {}

        return redirect('cart')