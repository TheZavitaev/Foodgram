import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET

from foodgram.settings import PAGINATOR_ITEMS_ON_THE_PAGE
from users.models import User
from .forms import RecipeForm
from .models import Recipe, IngredientValue, Purchase
from .utils import (get_tags_from_get, get_ingredients_for_views,
                    get_ingredients_for_js, get_ingredients_from_form,
                    save_recipe, create_shoplist_txt)


def index(request):
    recipes = Recipe.objects.select_related('author').prefetch_related(
        'tags', )
    tags_qs, tags_from_get = get_tags_from_get(request)

    if tags_qs:
        recipes = Recipe.objects.filter(tags__title__in=tags_qs).distinct()

    paginator = Paginator(recipes, PAGINATOR_ITEMS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'recipes/recipes_list.html',
        {'recipes': recipes, 'paginator': paginator,
         'page': page, 'tags': tags_from_get}
    )


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = get_ingredients_for_views(recipe)
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
        {'recipe': recipe, 'profile': profile,
         'ingredients': ingredients}
    )


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES or None)

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            save_recipe(ingredients=get_ingredients_from_form(request),
                        recipe=new_recipe)
            form.save_m2m()
            return redirect('recipe_view',
                            username=request.user.username,
                            recipe_id=new_recipe.id)

    form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


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
    return redirect('index')


@login_required
def recipe_edit(request, recipe_id, username):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(User, pk=recipe.author_id)

    if request.user != author:
        return redirect('recipe_view', username=username, recipe_id=recipe_id)

    form = RecipeForm(request.POST, instance=recipe,
                      files=request.FILES or None)

    if form.is_valid():
        IngredientValue.objects.filter(recipe=recipe).delete()
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        recipe.recipe_values.all().delete()

        save_recipe(ingredients=get_ingredients_from_form(request),
                    recipe=recipe)
        form.save_m2m()
        return redirect('recipe_view',
                        username=request.user.username,
                        recipe_id=recipe.id)

    return render(request,
                  'recipes/recipe_form.html',
                  {'form': form, 'recipe': recipe, 'author': author}
                  )


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    recipes_author = Recipe.objects.filter(author=profile)
    tags_qs, tags_from_get = get_tags_from_get(request)

    if tags_qs:
        recipes_author = Recipe.objects.filter(
            author=profile,
            tags__title__in=tags_qs).distinct()

    paginator = Paginator(recipes_author, PAGINATOR_ITEMS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html',
                  {'profile': profile, 'page': page,
                   'paginator': paginator, 'tags': tags_from_get}
                  )


def ingredients_for_js(request):
    data = get_ingredients_for_js(request)
    return JsonResponse(data, safe=False)


class PurchaseView(View):
    model = Purchase

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.purchase.get_purchases_list(self.request.user)

    def get(self, request):
        recipes_list = self.get_queryset()
        return render(request,
                      'recipes/shopList.html',
                      {'recipes_list': recipes_list}
                      )

    def post(self, request):
        json_data = json.loads(request.body.decode())
        recipe_id = json_data['id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        purchase = Purchase.purchase.get_user_purchase(user=request.user)
        data = {
            'success': 'true'
        }
        if not purchase.recipes.filter(id=recipe_id).exists():
            purchase.recipes.add(recipe)
            return JsonResponse(data)
        data['success'] = 'false'
        return JsonResponse(data)


@login_required()
def delete_purchase(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    purchase = Purchase.purchase.get(user=request.user)
    purchase.recipes.remove(recipe)
    return redirect('purchases')


@login_required()
@require_GET
def download_shop_list_txt(request):
    user = request.user
    filename = f'{user.username}_list.txt'
    content = create_shoplist_txt(user)
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
