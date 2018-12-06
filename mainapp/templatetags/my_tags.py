
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def discount(value, discount):
    if datetime.today().day == 25 and discount < 25:
        return float(value) * (1 - 25 / 100)
    elif datetime.today().day == 15 and discount < 15:
        return float(value) * (1 - 15 / 100)
    else:
        return float(value) * (1 - discount / 100)



@register.filter(name='spec_offer')
def spec_discount(value):
    if datetime.today().day == 25 and value < 25:
        return 25
    elif datetime.today().day == 15 and value < 15:
        return 15
    else:
        return value


@register.simple_tag(name='offer')
def spec_offer():
    if datetime.today().day == 25:
        return '25%'
    elif datetime.today().day == 15:
        return '15%'


