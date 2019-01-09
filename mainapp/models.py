from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

def validate_positive(value):
    if value < 0:
        raise ValidationError('Цена должна быть задана положительным числом!', code='invalid')


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование категории', max_length=200, unique=True)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=60,
                                  blank=True)
    desc = models.TextField(verbose_name='Подробное описание', blank=True)
    is_active = models.BooleanField(verbose_name='Запись активна', default=True)
    spec_discount = models.DecimalField(verbose_name='Специальная скидка', max_digits=4,
                                        decimal_places=2, default=0)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return 'catalog/%s' % self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'is_active']
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование продукта', max_length=150, unique=True,
                            error_messages={'required': 'Укажите название товара'})
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='products_images', blank=True)
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.SET_DEFAULT, default=10
    )
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=60,
                                  blank=True)
    desc = models.TextField(verbose_name='Подробное описание', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8,
                                decimal_places=2, validators=[validate_positive], default=0)
    discount = models.DecimalField(verbose_name='Скидка', max_digits=4,
                                decimal_places=2, default=0)
    is_active = models.BooleanField(verbose_name='Запись активна', default=True)

    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    modified = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'catalog/{self.category.name}/{self.name}'

    def _get_min_price(self):
        result = Product.objects.aggregate(models.Min('price'))
        return result['price__min']

    min_price = property(_get_min_price)

    def _get_max_price(self):
        result = Product.objects.aggregate(models.Max('price'))
        return result['price__max']

    max_price = property(_get_max_price)

    def __str__(self):
        return "{} ({}р., {}шт.)".format(self.name, self.price, self.quantity)

    class Meta:
        ordering = ['name', 'is_active', 'price']



