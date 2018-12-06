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

from mainapp.endpoints.products import (product_list,
                                    )

from mainapp.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductCreate, ProductUpdate,
                                    ProductDetail, mainapp_index, mainapp_Contacts,
                                    mainapp_registration, ProductDelete, category_product_list
                                    )

app_name = 'products'

endpointspatterns = [
    path('api/products/', product_list, name='list_api'),
]

urlpatterns = [
    path('', mainapp_index, name='start_page'),
    path('Contacts/', mainapp_Contacts, name='contacts'),
    path('registration/', mainapp_registration, name='registration'),
    path('catalog/', category_product_list, name='catalog'),
    # path('Catalog/Table/', products.mainapp_table, name='table'),
    # path('Catalog/Sofa/', products.mainapp_sofa, name='sofa'),
    # path('Catalog/Kitchen_set/', products.mainapp_kitchen_set, name='set'),
    # path('Catalog/Area/', products.mainapp_area_comfort, name='area_comfort'),
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('catalog/Tables/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('catalog/Sofas/<slug:slug>/',ProductDetail.as_view(), name='product_detail'),
    path('catalog/Sets/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    # re_path(r'^Catalog/(\w+)/<slug:title>$', products.product_detail, name='product_detail'),
    path('update/<slug:slug>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', ProductDelete.as_view(), name='delete'),
            ] + endpointspatterns





