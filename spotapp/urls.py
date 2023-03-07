from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('drink/<int:drink_id>', views.drink_detail, name='drink_detail'),
    path('drinks/', views.drinks, name='drinks'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
