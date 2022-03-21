from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.user_profile, name = 'profile'),
    path('edit-profile/', views.edit_user, name='edit')
]
