
from django import views
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name='index'), 
    path('', views.style),
    path('about/',views.about, name='about')
]




