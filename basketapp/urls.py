from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import basketapp.views as basketapp




app_name = 'basket'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<int:pk>', basketapp.basket_add, name='basket_add'),
    path('remove/<int:pk>', basketapp.basket_remove, name='basket_remove'),
]