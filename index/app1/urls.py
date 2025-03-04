from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [    
    path ('1', views.index),
    path ('2', views.index1),
]