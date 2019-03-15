from django import template
from meal.models import Category, Recipe

register = template.Library()

@register.inclusion_tag('meal/cats.html')
def get_category_list():
    return {'cats':Category.objects.all()}

@register.inclusion_tag('meal/recipe.html')
def get_ingredient_list(recipe = None):
    if (recipe is None):
        return {'ingredients': []}
    return {'ingredients': recipe.get_ingredients()}
