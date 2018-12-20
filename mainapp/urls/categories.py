from django.contrib import admin
from django.urls import path, re_path
from mainapp.views.categories import (CategoryGenericCreate, CategoryGenericUpdate,
                                      CategoryDetail, category_delete)


app_name = 'categories'

urlpatterns = [
    path('create/', CategoryGenericCreate.as_view(), name='create'),
    path('update/<slug:slug>/', CategoryGenericUpdate.as_view(), name='update'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('delete/<slug:title>/', category_delete, name='delete'),
]

