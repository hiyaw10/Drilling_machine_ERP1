# purchase/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='sub')
def sub(value, arg):
    """Subtracts arg from value."""
    return float(value) - float(arg)

@register.filter(name='mul')
def mul(value, arg):
    """Multiplies value by arg."""
    return float(value) * float(arg)