from django.contrib import admin
from .models import Category
from .models import Customer
from .models import Products
from .models import Orders

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phone', 'password')
    search_fields = ('email', 'firstName', 'lastName')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image')
    search_fields = ('name', )

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()