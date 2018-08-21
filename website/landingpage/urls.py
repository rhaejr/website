from django.urls import path
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('logout/', views.logout, name='logout'),
    
    
    ]