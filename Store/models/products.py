from django.db import models
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length = 50)
    price = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length = 500, default = '', null = True, blank = True)
    image = models.ImageField(upload_to = 'uploads/')

    @staticmethod
    def getProductsById(ids):
        return Products.objects.filter(id__in = ids)
    
    @staticmethod
    def getAllProducts():
        return Products.objects.all()
    
    @staticmethod
    def getAllProductsByCategory(cat_id):
        if cat_id:
            return Products.objects.filter(category = cat_id)
        else:
            return Products.getAllProducts()
