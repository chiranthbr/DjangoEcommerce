from django.urls import path, include
from django.contrib import auth
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views.home import Index, Store, categori
from .views.signup import Signup
from .views.login import Login, logout
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.cart import Cart, addToCarts
# from .middlewares.auth import auth_middleware

from . import views

urlpatterns = [
    path("", Store, name="homepage"),
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("check-out/", CheckOut.as_view(), name="checkout"),
    path("cart/", Cart.as_view(), name = "cart"),
    path("category/", categori, name="cats"),
    path("addToCart/", addToCarts, name="addtocarts"),
    # path("orders/", auth_middleware(OrderView.as_view()), name="orders"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)