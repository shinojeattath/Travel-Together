from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login, name = 'user_login'),
    path('homepage',views.homepage, name = 'homepage'),
    path('signup',views.signup, name = 'signup'),
    
]
