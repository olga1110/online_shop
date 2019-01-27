from django.contrib import admin
from django.urls import path, re_path

from mainapp.endpoints.products import product_list

from mainapp.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductCreate, ProductUpdate,
                                    ProductDetail, mainapp_index, mainapp_Contacts,
                                    product_delete, category_product_list, search_categories,
                                    )

app_name = 'products'

endpointspatterns = [
    path('api/products/', product_list, name='list_api'),
]

urlpatterns = [
                  path('', mainapp_index, name='start_page'),
                  path('contacts/', mainapp_Contacts, name='contacts'),
                  re_path(r'^catalog/((?P<page>\d+)|/)?$', category_product_list, name='catalog'),
                  path('create/', ProductGenericCreate.as_view(), name='create'),
                  re_path(r'^catalog/[^create delete update]\w+/(?P<slug>\w+)/$', ProductDetail.as_view(),
                          name='product_detail'),
                  re_path(r'^update/[^create delete update]\w+/(?P<slug>\w+)/$', ProductGenericUpdate.as_view(),
                          name='update'),
                  re_path(r'^delete/[^create delete update]\w+/(?P<slug>\w+)/$', product_delete, name='delete'),
                  path('categories/search/', search_categories, name='search_categories'),
              ] + endpointspatterns
