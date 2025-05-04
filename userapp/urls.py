from django.urls import path
from . import views                           #to import the index function from the views.py file

urlpatterns = [
    path('',views.index),                     #to map the index function to the root URL
]