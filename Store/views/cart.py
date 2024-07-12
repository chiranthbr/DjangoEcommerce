from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from Store.models.products import Products

class Cart(View):
    cart_items = {
        'a': {
            'name': "Mouse",
            'quantity': "3",
            'totalPrice': "1350",
        },

        'b': {
            'name': "Mouse 4",
            'quantity': "3",
            'totalPrice': "450",
        },

        'c': {
            'name': "Mouse 5",
            'quantity': "3",
            'totalPrice': "200",
        }
    }
    
    def Index(self, request):
        # cart = request.session.get('cart')
        # if not cart:
        #     request.session['cart'] = {}
        
        if request == "GET":
            return render(request, "cart.html", self.cart_items)
        
    def post(self, request):
        pass

    def get(self, request):
        total = sum([int(i['totalPrice']) for i in self.cart_items.values()])
        context = {'cart_items': self.cart_items, 'cart_total': str(total)}
        return render(request, "cart.html", context)
    
def addToCarts(request):
    param = request.GET.get('id', '')
    product = get_object_or_404(Products, id=param)
    if product:
        print(product)
        return JsonResponse({"message": "Successfully addedd!!"})
    return JsonResponse({"message": "Not added"})
