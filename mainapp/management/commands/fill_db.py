from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
import json, os

from userapp.models import ShopUser

super_user = ShopUser.objects.create_superuser('Olga',
                                               'a11os@yandex.ru', '11', age=27)
