from django.contrib.auth import get_user_model
from django.db import models

from recipes.models import Recipe


User = get_user_model()


class FavoriteRecipes(models.Model):
    """
    Модель понравившегося рецепта
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe'
    )

    class Meta:
        verbose_name = 'Любимый рецепт'
        verbose_name_plural = 'Любимые рецепты'


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
        return f'{self.user.username} подписан на {self.author.username}'

    class Meta:
        unique_together = ('user', 'author')
        verbose_name = 'Подписка на автора'
        verbose_name_plural = 'Подписки на авторов'


# TODO: добавить комментарии и рейтинговую систему
