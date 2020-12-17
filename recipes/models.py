from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Ingredient(models.Model):
    """
    Модель ингридиента
    """
    title = models.CharField(
        'Название ингредиента',
        max_length=255
    )
    dimension = models.CharField(
        'Единица измерения',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.title

# TODO: прикрутить python-usda для получения информации о составе и
#  энергетической ценности продуктов питания


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

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

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
        upload_to='media/'
    )
    description = models.TextField(
        'Описание рецепта',
        blank=False
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredient',
        through='IngredientValue',
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
    slug = models.SlugField(
        db_index=True
    )
    serving = models.PositiveSmallIntegerField(
        'Количество порций',
        help_text='в штуках',
        default=1
    )

    def __str__(self):
        return self.title

    @property
    def taglist(self):
        return list(self.tags.all())

    @property
    def ingredientslist(self):
        return list(self.ingredients.all())

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

# TODO: сделать теги для формирования подборок (кето, мексиканская,
#  итальянская, масленица, etc)


class IngredientValue(models.Model):
    """
    Модель количества ингридиентов в рецепте
    """
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='ingredient_values',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='recipe_values',
        on_delete=models.CASCADE
    )
    value = models.PositiveSmallIntegerField(
        'Количество ингредиентов',
        default=0
    )

    class Meta:
        verbose_name = 'Количество ингридиентов'
        verbose_name_plural = 'Количество ингридиентов'

    def __str__(self):
        return str(self.value)


class PurchaseManager(models.Manager):
    def counter(self, user):
        try:
            return super().get_queryset().get(user=user).recipes.count()
        except ObjectDoesNotExist:
            return 0

    def get_purchases_list(self, user):
        try:
            return super().get_queryset().get(user=user).recipes.all()
        except ObjectDoesNotExist:
            return []

    def get_user_purchase(self, user):
        try:
            return super().get_queryset().get(user=user)
        except ObjectDoesNotExist:
            purchase = Purchase(user=user)
            purchase.save()
            return purchase


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Покупатель')
    recipes = models.ManyToManyField(Recipe, verbose_name='Список рецептов')
    purchase = PurchaseManager()

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'

# TODO: прикрутить датасет с ценами продуктов питания (
#  https://data.gov.ru/taxonomy/term/74/datasets)

