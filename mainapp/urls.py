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
from django.urls import path, re_path
from . import views


# app_name = 'mainapp'

urlpatterns = [
    path('', views.mainapp_index, name='start_page'),
    path('Contacts/', views.mainapp_Contacts, name='contacts'),
    path('Registration/', views.mainapp_registration, name='registration'),
    # path('Catalog/Table/', views.mainapp_table, name='table'),
    # path('Catalog/Sofa/', views.mainapp_sofa, name='sofa'),
    # path('Catalog/Kitchen_set/', views.mainapp_kitchen_set, name='set'),
    # path('Catalog/Area/', views.mainapp_area_comfort, name='area_comfort'),
    path('create/', views.product_create, name='product_create'),
    path('categories/create/', views.category_create, name='category_create'),
    path('Catalog/Tables/<slug:title>/', views.product_detail, name='tables'),
    path('Catalog/Sofas/<slug:title>/', views.product_detail, name='sofas'),
    path('Catalog/Suite/<slug:title>/', views.product_detail, name='suite'),
    # re_path(r'^Catalog/(\w+)/<slug:title>$', views.product_detail, name='product_detail'),
    path('Catalog/<slug:title>/', views.category_detail, name='category'),
    path('Catalog/', views.mainapp_catalog, name='catalog'),
    path('update/<slug:title>/', views.product_update, name='update'),
]



