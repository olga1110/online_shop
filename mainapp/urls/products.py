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
from mainapp.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductCreate, ProductUpdate,
                                    ProductDetail, mainapp_index, mainapp_Contacts,
                                    mainapp_registration, product_detail, ProductDelete, category_product_list)


app_name = 'products'

urlpatterns = [
    path('', mainapp_index, name='start_page'),
    path('Contacts/', mainapp_Contacts, name='contacts'),
    path('Registration/', mainapp_registration, name='registration'),
    path('Catalog/', category_product_list, name='catalog'),
    # path('Catalog/Table/', products.mainapp_table, name='table'),
    # path('Catalog/Sofa/', products.mainapp_sofa, name='sofa'),
    # path('Catalog/Kitchen_set/', products.mainapp_kitchen_set, name='set'),
    # path('Catalog/Area/', products.mainapp_area_comfort, name='area_comfort'),
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('Catalog/Tables/<int:pk>/', ProductDetail.as_view(), name='tables'),
    path('Catalog/Sofas/<int:pk>/',ProductDetail.as_view(), name='sofas'),
    path('Catalog/Sets/<int:pk>/', ProductDetail.as_view(), name='suite'),
    # re_path(r'^Catalog/(\w+)/<slug:title>$', products.product_detail, name='product_detail'),
    path('update/<int:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
            ]





