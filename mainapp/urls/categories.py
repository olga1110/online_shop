from django.contrib import admin
from django.urls import path, re_path
from mainapp.views.categories import (CategoryGenericCreate, CategoryGenericUpdate,
                                      CategoryDetail, category_delete, CategoryFormSet,
                                      search_products)
from mainapp.endpoints.category import category_list, category_detail


app_name = 'categories'

urlpatterns = [
    path('create/', CategoryGenericCreate.as_view(), name='create'),
    path('update/<slug:slug>/', CategoryGenericUpdate.as_view(), name='update'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('delete/<slug:title>/', category_delete, name='delete'),
    path('edit/formsets/', CategoryFormSet.as_view(), name='formsets'),
    path('api/categories', category_list, name='category_list'),
    path('api/detail/<slug:title>/', category_detail, name='category_detail'),
    path('products/search/', search_products, name='search_products'),
]

