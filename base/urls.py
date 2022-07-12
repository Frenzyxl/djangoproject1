from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('forgot-password/', views.forgotPassword, name='forgot-password'),
]