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

from mainapp.endpoints.products import product_list

from mainapp.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductCreate, ProductUpdate,
                                    ProductDetail, mainapp_index, mainapp_Contacts,
                                    product_delete, category_product_list, search_categories,
                                    # mainapp_registration
                                    )

app_name = 'products'

endpointspatterns = [
    path('api/products/', product_list, name='list_api'),
]

urlpatterns = [
    path('', mainapp_index, name='start_page'),
    path('contacts/', mainapp_Contacts, name='contacts'),
    # path('registration/', mainapp_registration, name='registration'),
    re_path(r'^catalog/((?P<page>\d+)|/)?$', category_product_list, name='catalog'),
    path('create/', ProductGenericCreate.as_view(), name='create'),
    re_path(r'^catalog/[^create delete update]\w+/(?P<slug>\w+)/$', ProductDetail.as_view(), name='product_detail'),
    re_path(r'^update/[^create delete update]\w+/(?P<slug>\w+)/$', ProductGenericUpdate.as_view(), name='update'),
    re_path(r'^delete/[^create delete update]\w+/(?P<slug>\w+)/$', product_delete, name='delete'),
    path('categories/search/', search_categories, name='search_categories'),
            ] + endpointspatterns





