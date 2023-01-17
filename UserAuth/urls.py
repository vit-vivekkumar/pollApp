from django.urls import path
from django.contrib.auth import authenticate, login, logout
from . import views

# app_name = "UserDashboard"

urlpatterns = [
    path("register/", views.register_request, name="register"), 
    path("login/", views.login_request, name="login"),   
    path("logout", views.logout_request, name= "logout")     
]