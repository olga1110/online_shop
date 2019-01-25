from django.test import TestCase
from django.test import Client

from mainapp.views.products import category_product_list

from mainapp.models import Category, Product


class CategoryProductListTest(TestCase):
    client = Client()

    def setUp(self):
        Category.objects.create(name='test1_category')
        Category.objects.create(name='test2_category')
        Category.objects.create(name='test3_category')

    # def test_category_context(self):
    #     response = self.client.get('/catalog/')    #
    #     self.assertEqual(len(response.context['categories']), 3)

    def test_func(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.resolver_match.func, category_product_list)


class CategoryCRUDTest(TestCase):
    client = Client()

    def test_create_category(self):
        self.client.post('/catalog/create/', {'name': 'test1', 'short_desc': 'short_desc',
                                              'desc': 'full_desc'}, follow=True)
        cat1 = Category.objects.get(name='test1')
        self.assertEqual(cat1.desc, 'full_desc')

    def test_update_category(self):
        Category.objects.get_or_create(name='test1', short_desc='short_desc', desc='full_desc')
        self.client.post('/catalog/update/test1/', {'name': 'test1', 'short_desc': 'new short_desc',
                                                    'desc': 'full_desc'}, follow=True)
        cat1 = Category.objects.get(name='test1')
        self.assertEqual(cat1.short_desc, 'new short_desc')
