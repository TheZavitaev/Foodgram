from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from users.models import User
from .forms import RecipeForm
from .models import Recipe, Ingredient
from .utils import get_ingredients, get_tags


def index(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'recipes/recipes_list.html',
        {'recipes': recipes, 'paginator': paginator, 'page': page}
    )


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )
    ingredients = get_ingredients(recipe)
    if not request.user.is_authenticated:
        return render(
            request,
            'recipes/recipe_detail.html',
            {'recipe': recipe, 'ingredients': ingredients}
        )
    profile = get_object_or_404(User, username=username)
    return render(
        request,
        'recipes/recipe_detail.html',
        {'recipe': recipe, 'profile': profile, 'ingredients': ingredients}
    )


def recipe_add(request):
    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)
        form = RecipeForm(request.POST, files=request.FILES or None)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            # recipe.slug = unique_slug_generator(recipe)
            recipe.save()
            for tag in tags:
                recipe.tags.add(tag)
            for item in ingredients:
                recipe.ingredients.add(item.id)
            return redirect('recipe_list')
    else:
        form = RecipeForm()
        tags = {'Завтрак': 'Завтрак', 'Обед': 'Обед', 'Ужин': 'Ужин'}
    return render(request, 'recipes/recipe_form.html',
                  {'form': form, 'tags': tags})


@login_required
def recipe_delete(request, recipe_id, username):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    author = get_object_or_404(User, id=recipe.author_id)

    if request.user != author:
        return redirect(
            'recipe_view',
            username=username,
            recipe_id=recipe_id
        )

    recipe.delete()
    return redirect('recipe_list')


@login_required
def recipe_edit(request, recipe_id, username):
    editable_recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(User, pk=editable_recipe.author_id)

    if request.user != author:
        return redirect('recipe_view', username=username, recipe_id=recipe_id)

    form = RecipeForm(request.POST, instance=editable_recipe,
                      files=request.FILES or None)

    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)

        if form.is_valid():
            form.save()
            return redirect('recipe_view',
                            username=request.user.username,
                            recipe_id=recipe_id
                            )

    return render(request,
                  'recipes/recipe_form.html',
                  {'form': form, 'recipe': editable_recipe, 'author': author}
                  )


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    recipes_author = Recipe.objects.filter(author=profile)
    paginator = Paginator(recipes_author, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html',
                  {'profile': profile, 'page': page,
                   'paginator': paginator})


def ingredients_for_js(request):
    text = request.GET['query']
    ingredients = Ingredient.objects.filter(title__istartswith=text)
    ing_list = []
    ing_dict = {}
    for ing in ingredients:
        ing_dict['title'] = ing.title
        ing_dict['dimension'] = ing.dimension
        ing_list.append(ing_dict)

    return JsonResponse(ing_list, safe=False)


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
