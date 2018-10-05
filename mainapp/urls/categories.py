from django.contrib import admin
from django.urls import path, re_path
from mainapp.views.categories import (CategoryGenericCreate, CategoryGenericUpdate, CategoryDelete,
                                      CategoryDetail, category_detail)


app_name = 'categories'

urlpatterns = [
    path('categories/create/', CategoryGenericCreate.as_view(), name='create'),
    path('update/<int:pk>/', CategoryGenericUpdate.as_view(), name='update'),
    path('Catalog/<int:pk>/', CategoryDetail.as_view(), name='category'),
    path('categories/delete/<int:pk>/', CategoryDelete.as_view(), name='delete'),
]

