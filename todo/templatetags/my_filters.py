from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='my_upper')
def to_upper(value, number):
    s = ''
    for i, v in enumerate(value, 1):
        if v.isalpha() and i <= int(number):
            s += v.upper()
        else:
            s += v
    return s


@register.filter
def my_filter(value):
    text = f"<b>{value}</b>"
    return mark_safe(text)
