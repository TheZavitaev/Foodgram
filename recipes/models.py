from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Ingredient(models.Model):
    """
    Модель ингридиента
    """
    title = models.CharField(
        'Название ингредиента',
        max_length=255
    )
    measure = models.CharField(
        'Единица измерения',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.title

# TODO: добавить метаданные к описанию моделей для читаемости в админпанели


class Tag(models.Model):
    """
    Модель тега
    """
    tag_options = {
        'breakfast': ['orange', 'Завтрак'],
        'lunch': ['green', 'Обед'],
        'dinner': ['purple', 'Ужин']
    }

    TAG_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
    ]
    title = models.CharField(
        max_length=10,
        choices=TAG_CHOICES,
        verbose_name='Название тега'
    )

    def __str__(self):
        return self.title

    @property
    def color(self):
        return self.tag_options[self.title][0]

    @property
    def name(self):
        return self.tag_options[self.title][1]


class Recipe(models.Model):
    """
    Модель рецепта
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_author'
    )
    title = models.CharField(
        'Название рецепта',
        max_length=255,
        blank=False
    )
    image = models.ImageField(
        'Изображение',
        upload_to='recipe_images/'
    )
    description = models.TextField(
        'Описание рецепта',
        blank=False
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredient',
        through='IngredientAmount',
        through_fields=('recipe', 'ingredient')
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipe_tag'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        help_text='в минутах',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    def get_ingredients(self):
        return '\n'.join(
            self.ingredients.all().values_list('title', flat=True))
    get_ingredients.short_description = 'Ингредиенты'

    def get_tags(self):
        return '\n'.join(
            self.tags.all().values_list('title', flat=True))
    get_tags.short_description = 'Теги'

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

# TODO: добавить метаданные к описанию моделей для читаемости в админпанели


class IngredientAmount(models.Model):
    """
    Модель количества ингридиентов в рецепте
    """
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='ingredient_amount',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='recipe_ingredient_amount',
        on_delete=models.CASCADE
    )
    amount = models.PositiveSmallIntegerField(
        'Количество ингредиентов',
        default=0
    )

# TODO: добавить метаданные к описанию моделей для читаемости в админпанели


class Cart(models.Model):
    shopper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopper_carts',
        verbose_name='Покупатель'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_carts',
        verbose_name='Список рецептов'
    )

# TODO: подумать над тем, как это отрисовывать
    def __str__(self):
        return self.recipe.title

    class Meta:
        unique_together = ('shopper', 'recipe')
