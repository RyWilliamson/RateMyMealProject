from django import template
from meal.models import Category, Recipe

register = template.Library()

@register.inclusion_tag('meal/cats.html')
def get_category_list():
    return {'cats':Category.objects.all()}

@register.inclusion_tag('meal/rectest.html')
def get_category_list2():
    return {'cats':Category.objects.all()}
