from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import userapp.views as userapp
import mainapp.urls


app_name = 'auth'

urlpatterns = [
    path('login/', userapp.LoginView.as_view(), name='login'),
    path('logout/', userapp.logout, name='logout'),
    path('register/', userapp.RegisterView.as_view(), name='register'),
    path('edit/', userapp.edit, name='edit'),
]


