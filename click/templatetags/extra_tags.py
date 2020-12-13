from django import template

register = template.Library()

@register.filter(name='split')
def split(value,arg):
    return value.split(arg)

@register.filter(name='hasAttribute')
def hasAttribute(value,arg):
    return hasattr(value, arg)

@register.filter(name='times')
def times(number):
    number = round(number)
    return range(number)
