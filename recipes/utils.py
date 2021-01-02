from urllib.parse import unquote

from django.db.models import Sum
from django.shortcuts import get_object_or_404

from .models import Ingredient, Tag, IngredientValue, Purchase


def get_ingredients_for_js(request):
    query = unquote(request.GET.get('query'))
    return list(Ingredient.objects.filter(
        title__icontains=query).values('title', 'dimension'))


def get_ingredients_from_form(request):
    ingredients = {}

    for key in request.POST:
        if key.startswith('nameIngredient'):
            ing_number = key[15:]
            ingredients[request.POST[key]] = request.POST[
                f'valueIngredient_{ing_number}'
            ]

    return ingredients


# def get_ingredients_from_form(request):
#     ingredients = {}
# этот вариант дает ошибку
#     for key, ingredient_name in request.POST.items():
#         if 'nameIngredient' in key:
#             _ = key.split('_')
#             ingredients[ingredient_name] = int(
#                 request.POST[f'valueIngredient_{_[1]}']
#             )
#
#     return ingredients


def save_recipe(ingredients, recipe):
    recipe_ingredients = []

    for title, value in ingredients.items():
        ingredient = get_object_or_404(Ingredient, title=title)
        rec_ingredient = IngredientValue(
            value=value, ingredient=ingredient, recipe=recipe
        )
        recipe_ingredients.append(rec_ingredient)

    IngredientValue.objects.bulk_create(recipe_ingredients)


def get_tags_from_get(request):
    tags_from_get = []

    if 'tags' in request.GET:
        tags_from_get = request.GET.get('tags')
        _ = tags_from_get.split(',')
        tags_qs = Tag.objects.filter(title__in=_).values('title')
    else:
        tags_qs = False

    return [tags_qs, tags_from_get]


def create_shoplist_txt(user):
    recipes = Purchase.purchase.get_purchases_list(user).values(
        'ingredients__title', 'ingredients__dimension'
    )
    ingredients = recipes.annotate(Sum('recipe_values__value')).order_by()
    products = [
        (f'{i["ingredients__title"]} ({i["ingredients__dimension"]}) -'
         f' {i["recipe_values__value__sum"]}')
        for i in ingredients]
    content = 'Продукт (единицы) - количество \n \n' + '\n'.join(products)

    return content
