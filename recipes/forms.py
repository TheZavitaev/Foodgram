from django.forms import (ModelForm, ModelMultipleChoiceField,
                          CheckboxSelectMultiple, CharField, IntegerField,
                          MultipleChoiceField, ImageField, Textarea)
from recipes.models import Ingredient, Recipe, Tag


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('title', 'dimension')


class RecipeForm(ModelForm):
    TAG_CHOICES = (
        ('Завтрак', 'orange'),
        ('Обед', 'green'),
        ('Ужин', 'purple'),
    )
    title = CharField(max_length=256)
    tags = MultipleChoiceField(widget=CheckboxSelectMultiple,
                               choices=TAG_CHOICES,
                               )
    cooking_time = IntegerField(min_value=1)
    description = CharField(widget=Textarea(attrs={'class': 'form__textarea'}))
    image = ImageField()

    class Meta:
        model = Recipe
        fields = ('title', 'cooking_time', 'description', 'image')
