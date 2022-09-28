from django.contrib import admin
from django.urls import path
from blogs import views
urlpatterns = [
   
    path('', views.index, name="home"),
    path('about', views.about, name="AboutUs"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="ContactUs"),
    
  
]
