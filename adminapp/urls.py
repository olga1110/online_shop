from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'admin'
urlpatterns = [
    path('', adminapp.admin_page, name='admin_page'),
    path('users/', adminapp.UserList.as_view(), name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<slug:slug>/', adminapp.user_update, \
         name='user_update'),
    path('users/delete/<slug:slug>/', adminapp.user_delete, \
         name='user_delete'),
    path('catalog/create/', adminapp.category_create, \
         name='category_create'),
    path('catalog/', adminapp.CategoryList.as_view(), name='category'),
    path('catalog/update/<slug:slug>/', adminapp.category_update, \
         name='category_update'),
    path('products/', adminapp.ProductList.as_view(), name='product_list'),
    path('catalog/delete/<slug:slug>/', adminapp.category_delete, \
         name='category_delete'),
    path('products/create/category/<slug:slug>/', adminapp.product_create, \
         name='product_create'),
    path('products/category/<slug:slug>/', adminapp.products, \
         name='products'),
    path('products/<slug:slug>/', adminapp.product_read, \
         name='product_read'),
    path('products/update/<slug:slug>/', adminapp.product_update, \
         name='product_update'),
    path('products/delete/<slug:slug>/', adminapp.product_delete, \
         name='product_delete'),
]
