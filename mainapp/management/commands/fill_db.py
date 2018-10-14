from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Category, Product
import json, os

from userapp.models import ShopUser

# super_user = ShopUser.objects.create_superuser('Olga',
#                                                'a11os@yandex.ru', '11', age=27)

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, required=True)

    def handle(self, *args, **options):
        try:
            with open('data.json', 'r') as file:
                for row in json.load(file):
                    Product.objects.get_or_create(**row)
        except Exception as err:
            raise CommandError(err)

