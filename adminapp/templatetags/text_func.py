
from django import template

register = template.Library()


@register.filter
def startswith(value, str):
    if value.startswith(str):
        return True
    else:
        return False









