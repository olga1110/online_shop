from django.test import TestCase, override_settings
from django.test import Client

from .models import Basket
from userapp.models import ShopUser
from mainapp.models import Category, Product


class BasketModelTest(TestCase):
    def setUp(self):
        user = ShopUser.objects.get_or_create(username='testuser')[0]
        category = Category.objects.create(name='category1')
        product1 = Product.objects.create(name='product1', category=category, price=100)
        product2 = Product.objects.create(name='product2', category=category, price=200)
        product3 = Product.objects.create(name='product3', category=category, price=300)
        basket1 = Basket.objects.create(user=user, product=product1, quantity=5)
        basket2 = Basket.objects.create(user=user, product=product2, quantity=5)
        basket3 = Basket.objects.create(user=user, product=product3, quantity=5)

    def test_product_cost(self):
        basket = Basket.objects.first()
        self.assertEqual(basket.product_cost, 500)

    def test_total_quantity(self):
        basket = Basket.objects.first()
        self.assertEqual(basket.total_quantity, 15)

    def test_total_cost(self):
        basket = Basket.objects.first()
        self.assertEqual(basket.total_cost, 3000)


class AccessTest(TestCase):
    client = Client()

    def test_basket_authorized(self):
        self.client.force_login(ShopUser.objects.get_or_create(username='testuser')[0])
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    def test_basket_unauthorized(self):
        response = self.client.get('/basket/', follow=True)
        self.assertEqual(response.redirect_chain, [('/auth/login/?next=/basket/', 302)])
