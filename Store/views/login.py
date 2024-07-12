from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from Store.models.customer import Customer
from django.views import View

class Login(View):
    returnURL = None

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # user = authenticate(request, email = email, password = password)
        errorMSG = ''

        customer = Customer.getCustomerByEmail(email)
        name = customer.firstName + " " + customer.lastName
        print(customer, " jdj")

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                if Login.returnURL:
                    return HttpResponseRedirect(Login.returnURL)
                else:
                    Login.returnURL = None
                    return render(request, 'home.html', {"name": name})
            else:
                errorMSG = 'invalid password'
        else:
            errorMSG = 'invalid Username and password'

        print(email, password)
        return render(request, 'login.html', {'error': errorMSG})

        # if user is not None:
        #     login(request, user)
        #     print("logged in")
        #     if Login.returnURL:
        #         return HttpResponseRedirect(Login.returnURL)
        #     else:
        #         Login.returnURL = None
        #         return redirect('homepage')
        # else:
        #     customer = Customer.getCustomerByEmail(email)
        #     if customer:
        #         errorMSG = 'Invalid password'
        #     else:
        #         errorMSG = 'Invalid user'
        # print(email, password)
        # return render(request, 'login.html', {'error': errorMSG})
    
def logout(request):
    request.session.clear()
    return redirect('login')