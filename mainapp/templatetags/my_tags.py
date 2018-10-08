# ///////////////////////////Свой шаблон/////////////////////////////////////////////////////
from django import template
register = template.Library()

@register.filter
def discount(value, discount):
    return value *(1 - discount / 100)