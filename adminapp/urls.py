from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'admin'
urlpatterns = [
    path('', adminapp.admin_page, name='admin_page'),
    path('users/', adminapp.UserList.as_view(), name='users'),
    path('users/create/', adminapp.UserCreate.as_view(), name='user_create'),
    path('users/update/<slug:slug>/', adminapp.UserUpdate.as_view(), \
         name='user_update'),
    path('users/delete/<slug:title>/', adminapp.user_delete, \
         name='user_delete'),

    path('catalog/create/', adminapp.CategoryCreate.as_view(), \
         name='category_create'),
    path('catalog/', adminapp.CategoryList.as_view(), name='category'),
    path('catalog/update/<slug:slug>/', adminapp.CategoryUpdate.as_view(), \
         name='category_update'),
    path('catalog/delete/<slug:title>/', adminapp.category_delete, \
         name='category_delete'),

    path('products/', adminapp.ProductList.as_view(), name='product_list'),
    path('products/category/<slug:title>/', adminapp.products, \
         name='products'),
    # path('products/<slug:title>/', adminapp.product_read, \
    #      name='product_detail'),

    path('products/create/', adminapp.ProductCreate.as_view(), \
         name='product_create'),
    path('products/update/<slug:slug>/', adminapp.ProductUpdate.as_view(), \
         name='product_update'),
    path('products/delete/<slug:title>/', adminapp.product_delete, \
         name='product_delete'),
]
