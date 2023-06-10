from django.contrib import admin
from django.urls import path
from .views import home, login , register
urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('', home),
]