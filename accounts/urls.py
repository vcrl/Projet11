from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('signin/', views.loginuser, name="loginuser"),
    path('profile/', views.displayprofile, name="profile"),
    path('', views.return_to_frontpage, name="frontpage")
]