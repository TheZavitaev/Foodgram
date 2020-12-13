from django import template

from social.models import FavoriteRecipes, SubscribeToAuthor
from recipes.models import Cart

register = template.Library()


@register.filter(name='is_favorite')
def is_favorite(recipe_id, user_id):
    return FavoriteRecipes.objects.filter(
        user_id=user_id, recipe_id=recipe_id).exists()


@register.filter(name='is_following')
def is_following(author, user):
    return SubscribeToAuthor.objects.filter(user=user, author=author).exists()


@register.filter(name='plural_recipes')
def plural_recipe(number):
    if number % 10 == 1 and number not in (11, 111):
        ending = ''
    elif 1 < number % 10 < 5 and number not in (12, 13, 14, 112, 113, 114):
        ending = 'а'
    else:
        ending = 'ов'
    return ending


@register.filter(name='recipe_in_cart')
def recipe_in_cart(recipe, user):
    """
    Проверка наличия рецепта в корзине
    """
    return Cart.objects.filter(shopper=user, recipe=recipe).exists()
