from django import forms
from django.forms import ModelForm

from recipes.models import Recipe, Ingredient, IngredientValue, Tag


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'cooking_time',
                  'description', 'image'
                  )
        widgets = {'tags': forms.CheckboxSelectMultiple()}

    # def __init__(self, data=None, *args, **kwargs):
    #     if data is not None:
    #         data = data.copy()
    #         data.update({'ingredients_ids': data.getlist('nameIngredient')})
    #     self.ingredients_dict = None
    #     super().__init__(data=data, *args, **kwargs)
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     ids = self.data['ingredients_ids']
    #     errors = []
    #
    #     if not ids:
    #         error = forms.ValidationError('Необходимо указать ингредиенты')
    #         self.add_error('ingredients', error)
    #     #
    #     # try:
    #     #     count = Ingredient.objects.filter(pk__in=ids).count()
    #     #     less_zero_quantity_values = [val for val in quantity if
    #     #                                  int(val) < 0]
    #     #
    #     #     if less_zero_quantity_values:
    #     #         errors.append(forms.ValidationError(
    #     #             'Отрицательное количество ингредиентов '
    #     #             'не может быть добавлено'
    #     #         ))
    #     #     if not count == len(ids):
    #     #         raise ValueError
    #     #
    #     # except ValueError:
    #     #     errors.append(forms.ValidationError(
    #     #         'В форму переданы некоректные данные. '
    #     #         'Возможно, вы попытались добавить несуществующий ингредиент '
    #     #         'или ввели количество не в виде числа. \
    #     #         Не надо так.'
    #     #     ))
    #     #
    #     # except:
    #     #     errors.append(forms.ValidationError(
    #     #         'Произошла непредвиденная ошибка. '
    #     #         'Попробуйте заполнить форму еще раз.'))
    #     #
    #     # for erorr in errors:
    #     #     self.add_error('ingredients', erorr)
    #     #
    #     # self.ingredients_dict = dict(zip(ids, quantity))
    #
    #     return cleaned_data
