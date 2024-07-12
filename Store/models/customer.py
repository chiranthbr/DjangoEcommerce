from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def getCustomerByEmail(e):
        try:
            return Customer.objects.get(email = e)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    
    def getNameById(id):
        try:
            return Customer.objects.get(id = id)
        except:
            return None
        

# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models

# class CustomerManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
# class Customer(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     phone = models.CharField(max_length=10)
#     is_active = models.BooleanField(default=True)
    
#     objects = CustomerManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []  # If you have additional required fields, list them here

#     def register(self):
#         self.save()

#     def __str__(self):
#         return self.first_name + " " + self.last_name
    
#     def getCustomerByEmail(e):
#         try:
#             return Customer.objects.get(email = e)
#         except:
#             return False
        
#     def isExists(self):
#         if Customer.objects.filter(email = self.email):
#             return True
#         return False
    
#     def getNameById(id):
#         try:
#             return Customer.objects.get(id = id)
#         except:
#             return None
    