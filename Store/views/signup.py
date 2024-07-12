from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from Store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        firstName = postData.get('firstName')
        lastName = postData.get('lastName')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'firstName': firstName,
            'lastName': lastName,
            'phone': phone,
            'email': email,
        }
        errorMSG = None

        customer = Customer(firstName = firstName,
                            lastName = lastName,
                            phone = phone,
                            email = email,
                            password = password)
        
        errorMSG = self.validateCustomer(customer)

        if not errorMSG:
            print(firstName, lastName, phone, email, password)
            customer.password = make_password(customer.password)
            customer.isLoggedIn = True
            customer.save()
            return redirect('homepage')
        else:
            data = {
                'error': errorMSG,
                'values': value
            }
            print("errorMSG: ", errorMSG)
            return render(request, 'signup.html', data)
        
    def validateCustomer(self, customer):
        if (not customer.firstName):
            return 'Please enter first name'
        elif not customer.lastName:
            return 'Please enter last name'
        elif not customer.phone:
            return 'Please enter phone number'
        elif not customer.email:
            return 'Please enter email'
        elif not customer.password:
            return 'Please enter password'
        elif Customer.objects.filter(email=customer.email).exists():
            return 'Email Address Already Registered'
        return None