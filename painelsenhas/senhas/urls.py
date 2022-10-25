from django.contrib import admin
from django.urls import path
from senhas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('senhas', views.exibir, name='exibir'),
]