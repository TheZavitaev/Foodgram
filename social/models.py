from django.contrib.auth import get_user_model
from django.db import models

from recipes.models import Recipe


User = get_user_model()

# TODO: добавить метаданные к описанию моделей для читаемости в админпанели


class FavoriteRecipes(models.Model):
    """
    Модель понравившегося рецепта
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipes = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites_recipes'
    )

# TODO: добавить метаданные к описанию моделей для читаемости в админпанели


class SubscribeToAuthor(models.Model):
    """
    Модель любимого автора
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    def __str__(self):
        return f'follower - {self.user} | following - {self.author}'

    class Meta:
        unique_together = ('user', 'author')


# TODO: добавить комментарии и рейтинговую систему
