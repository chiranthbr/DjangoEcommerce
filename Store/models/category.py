from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def getAllCategories():
        return Category.objects.all()
    
    def __str__(self) -> str:
        return self.name
    