from django.forms import ModelForm
from recipes.models import Ingredient, Recipe


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('title', 'dimension')


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'cooking_time', 'description', 'image')
