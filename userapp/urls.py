from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import userapp.views as userapp
import mainapp.urls

urlpatterns = [
    url(r'^login/$', userapp.login, name='login'),
    url(r'^logout/$', userapp.logout, name='logout'),
]
