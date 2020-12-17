import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic.base import View

from recipes.models import Recipe
from social.utils import get_filters
from social.models import FavoriteRecipes, SubscribeToAuthor

from users.models import User


@login_required
def favorites(request, username):
    recipes = Recipe.objects.filter(favorite_recipe__user=request.user)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes,
        'paginator': paginator,
        'page': page,
        'username': username
    })


@login_required
def add_favorites(request):
    recipe_id = json.loads(request.body).get('id')
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    FavoriteRecipes.objects.get_or_create(user=request.user, recipe=recipe)
    return JsonResponse({'success': True})


@login_required
def remove_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    removed = FavoriteRecipes.objects.filter(
        user=request.user, recipe=recipe).delete()
    return JsonResponse({'success': True})


@login_required
def my_subscriptions(request, username):
    user = get_object_or_404(User, username=username)
    subscriptions = User.objects.prefetch_related('recipe_author').filter(
        following__user=user.id)
    paginator = Paginator(subscriptions, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'recipes/subscription_list.html',
        {'page': page, 'paginator': paginator}
    )


@login_required
def subscribe(request):
    author_id = json.loads(request.body).get('id')
    author = get_object_or_404(User, pk=author_id)
    if request.user != author:
        SubscribeToAuthor.objects.get_or_create(user=request.user,
                                                author=author)
    return JsonResponse({'success': True})


@login_required
def unsubscribe(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    if request.user != author:
        SubscribeToAuthor.objects.filter(user=request.user,
                                         author=author).delete()
    return JsonResponse({'success': True})
