from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('home/', views.landing, name='landing'),
    path('business/', views.business, name='business')
]
