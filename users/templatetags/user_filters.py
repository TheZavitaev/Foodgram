from django import template

from recipes.models import Cart
from social.models import FavoriteRecipes, SubscribeToAuthor

register = template.Library()


@register.filter
def addclass(field, css):
    """
    Формирование тэгов для GET запроса
    """
    return field.as_widget(attrs={"class": css})


@register.filter(name='recipe_in_cart')
def recipe_in_cart(recipe, user):
    """
    Проверка наличия рецепта в корзине
    """
    return Cart.objects.filter(shopper=user, recipe=recipe).exists()


@register.filter(name='is_following')
def is_following(author, user):
    return SubscribeToAuthor.objects.filter(user=user, author=author).exists()


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
    return FavoriteRecipes.objects.filter(user=user, recipes=recipe).exists()
