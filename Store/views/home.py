from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from Store.models.products import Products
from Store.models.category import Category
from Store.models.customer import Customer
from django.views import View

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        return HttpResponseRedirect(f'/Store{request.get_full_path()[1:]}')
    
def Store(request):

    # cart = request.session.get('cart')
    # if not cart:
    #     request.session['cart'] = {}
    products = None
    categories = Category.getAllCategories()
    categoryId = request.GET.get('category')
    # custId = request.session.get('customer')
    # print(custId)
    # customer = Customer.getNameById(custId)
    # name = customer.firstName + customer.lastName

    if categoryId:
        products = Products.getAllProductsByCategory(categoryId)
    else:
        products = Products.getAllProducts()

    data = {}
    data['products'] = products
    data['categories'] = categories

    for i in products:
        print(i.image.url)
    # data['name'] = name

    return render(request, 'home.html', data)

def categori(request):
    query_param = request.GET.get('q', '')
    cat = get_object_or_404(Category, name=query_param)
    cat_id = cat.id
    prods = Products.getAllProductsByCategory(cat_id = cat_id)
    return render(request, 'categories.html', {'productsByCategory': prods, 'category': cat})
    pass
