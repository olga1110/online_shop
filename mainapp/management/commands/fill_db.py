from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
import json
import os

from userapp.models import ShopUser

JSON_PATH = 'mainapp/static/mainapp/files'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')
        for category in categories.values():
            new_category = Category(**category)
            new_category.save()

        # for product in products:
        #     category_name = product["category"]
        #     # Получаем категорию по имени
        #     _category = Category.objects.get(name=category_name)
        #     # Заменяем название категории объектом
        #     product['category'] = _category
        #     new_product = Product(**product)
        #     new_product.save()

# super_user = ShopUser.objects.create_superuser('Olga',
#                                                'a11os@yandex.ru', '11', age=27)
