from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from recipes.models import Recipe, Ingredient


class RecipeForm(ModelForm):
    title = forms.CharField(max_length=256)
    cooking_time = forms.IntegerField(min_value=1)

    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'cooking_time',
                  'description', 'image'
                  )
        widgets = {'tags': forms.CheckboxSelectMultiple()}

    # def clean(self):
    #     ing_ids = []
    #
    #     for items in self.data.keys():
    #
    #         if 'nameIngredient' in items:
    #             name, ing_id = items.split('_')
    #             ing_ids.append(ing_id)
    #
    #     for ing_id in ing_ids:
    #         title = self.data.get(f'nameIngredient_{ing_id}')
    #         dimension = self.data.get(f'unitsIngredient_{ing_id}')
    #         is_exists = Ingredient.objects.filter(
    #             title=title[0], dimension=dimension
    #         ).exists()
    #
    #         if not is_exists:
    #             raise ValidationError(
    #                 'Выберите ингредиент из предложенного списка'
    #             )

    def clean_tags(self):
        pass
