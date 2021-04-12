from django.contrib import admin
from django.urls import path
from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('mentions/', views.mentions, name="mentions"),
    path('sentry-debug/', trigger_error),
]
