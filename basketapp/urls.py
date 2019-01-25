from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import basketapp.views as basketapp

app_name = 'basket'

urlpatterns = [
    path('', basketapp.BasketList.as_view(), name='basket'),
    path('add/<int:pk>', basketapp.basket_add, name='basket_add'),
    path('order/', basketapp.order_send, name='order_send'),
    path('remove/<int:pk>', basketapp.basket_remove, name='basket_remove'),
    path('remove/', basketapp.basket_remove_all, name='basket_remove_all'),
]
