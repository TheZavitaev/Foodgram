from django import template
from django.shortcuts import get_object_or_404

from social.models import FavoriteRecipes, SubscribeToAuthor
from recipes.models import Purchase, Recipe

register = template.Library()


@register.filter(name='purchase_list')
def purchase_list(user_id):
    return Purchase.purchase.get_purchases_list(user_id)


@register.filter(name='recipe_in_cart')
def recipe_in_cart(recipe_id, user_id):
    recipes = purchase_list(user_id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe in recipes:
        return True


@register.filter(name='plural_recipes')
def plural_recipe(number):
    if number % 10 == 1 and number not in (11, 111):
        ending = ''
    elif 1 < number % 10 < 5 and number not in (12, 13, 14, 112, 113, 114):
        ending = 'а'
    else:
        ending = 'ов'
    return ending


@register.filter
def formatting_tags(request, tag):
    if 'tags' in request.GET:
        tags = request.GET.get('tags')
        tags = tags.split(',')
        if tag not in tags:
            tags.append(tag)
        else:
            tags.remove(tag)
        if '' in tags:
            tags.remove('')
        result = ','.join(tags)
        return result
    return tag
