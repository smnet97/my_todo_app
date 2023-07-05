from django import template

register = template.Library()

from ..models import CategoryModel


@register.simple_tag
def get_categories(order_value=None):
    if not order_value:
        return CategoryModel.objects.all()
    else:
        return CategoryModel.objects.all().order_by(order_value)


@register.inclusion_tag('layouts/cat_navbar.html')
def category():
    objects = CategoryModel.objects.all()

    return {
        'cats': objects
    }
