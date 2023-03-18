from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('geo1', views.coords_send),
]