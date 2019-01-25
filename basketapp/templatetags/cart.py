from django import template
from basketapp.models import Basket

register = template.Library()


@register.filter(name='total_quantity')
def quantity(value):
    if Basket.objects.filter(user=value).count():
        return Basket.objects.filter(user=value)[0].total_quantity
    return ''
