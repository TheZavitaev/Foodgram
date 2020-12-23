from django import template

from social.models import FavoriteRecipes, SubscribeToAuthor

register = template.Library()


@register.filter(name='is_favorite')
def is_favorite(recipe_id, user_id):
    return FavoriteRecipes.objects.filter(
        user_id=user_id, recipe_id=recipe_id).exists()


@register.filter(name='is_subscribed')
def is_subscribed(author, user_id):
    return SubscribeToAuthor.objects.filter(
        user=user_id, author=author).exists()
