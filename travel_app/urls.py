from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.user_login, name = 'user_login'),
    path('homepage',views.homepage, name = 'homepage'),
    path('signup',views.signup, name = 'signup'),
    path('jammu',views.jammu, name = 'jammu'),
    path('booking', views.booking,name = 'booking'), 
    path('idukki',views.idukki, name = 'idukki'),
    path('Delhi',views.Delhi, name = 'Delhi'),
    path('profile',views.profile, name = 'profile'),
    path('cancel',views.cancelFunc,name='cancelFunc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)