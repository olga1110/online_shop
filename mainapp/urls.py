"""web_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
# from first.views import index

urlpatterns = [
    path('', views.mainapp_index, name='main'),
    path('Catalog/', views.mainapp_catalog, name='catalog'),
    path('Contacts/', views.mainapp_Contacts, name='contacts'),
    path('Registration/', views.mainapp_registration, name='registration'),
    path('Catalog/Table/', views.mainapp_table, name='table'),
    path('Catalog/Sofa/', views.mainapp_sofa, name='sofa'),
    path('Catalog/Kitchen_set/', views.mainapp_kitchen_set, name='set'),
    path('Catalog/Area/', views.mainapp_area_comfort, name='area_comfort'),
]



