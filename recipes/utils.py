import os

from django.contrib.staticfiles import finders
from django.shortcuts import get_object_or_404

from foodgram import settings
from .models import Ingredient, Tag, IngredientValue


def get_ingredients_for_js(request):
    text = request.GET['query']
    ingredients = Ingredient.objects.filter(title__istartswith=text)
    ing_list = []
    ing_dict = {}
    for ing in ingredients:
        ing_dict['title'] = ing.title
        ing_dict['dimension'] = ing.dimension
        ing_list.append(ing_dict)
    return ing_list


def get_ingredients_for_views(recipe):
    ingredients = []
    for ingredient in recipe.ingredients.all():
        value = ingredient.ingredient_values.get(recipe=recipe)
        ingredients.append((ingredient.title, value, ingredient.dimension))
    return ingredients


def get_ingredients_from_form(request):
    ingredients = {}
    for key, ingredient_name in request.POST.items():
        if 'nameIngredient' in key:
            _ = key.split('_')
            ingredients[ingredient_name] = int(
                request.POST[f'valueIngredient_{_[1]}']
            )
    return ingredients


def save_recipe(ingredients, recipe):
    recipe_ingredients = []

    for title, value in ingredients.items():
        ingredient = get_object_or_404(Ingredient, title=title)
        rec_ingredient = IngredientValue(
            value=value, ingredient=ingredient, recipe=recipe
        )
        recipe_ingredients.append(rec_ingredient)
    IngredientValue.objects.bulk_create(recipe_ingredients)


def get_tags(request):
    tags = []
    for key in request.POST.getlist('tag'):
        tags.append(get_object_or_404(Tag, id=int(key)))
    return tags


def get_tags_from_get(request):
    tags_from_get = []
    if 'tags' in request.GET:
        tags_from_get = request.GET.get('tags')
        _ = tags_from_get.split(',')
        tags_qs = Tag.objects.filter(title__in=_).values('title')
    else:
        tags_qs = False
    return [tags_qs, tags_from_get]


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
        mUrl = settings.MEDIA_URL
        mRoot = settings.MEDIA_ROOT

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path
