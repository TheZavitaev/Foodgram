import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from foodgram.settings import PAGINATOR_ITEMS_ON_THE_PAGE
from recipes.models import Recipe
from recipes.utils import get_tags_from_get
from social.models import FavoriteRecipes, SubscribeToAuthor
from users.models import User


@login_required
def favorites(request, username):
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(favorite_recipe__user=request.user)
    tags_qs, tags_from_get = get_tags_from_get(request)

    if tags_qs:
        recipes = Recipe.objects.filter(favorite_recipe__user=request.user,
                                        tags__title__in=tags_qs).distinct()

    paginator = Paginator(recipes, PAGINATOR_ITEMS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes, 'paginator': paginator, 'page': page,
        'username': user, 'tags': tags_from_get
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
    FavoriteRecipes.objects.filter(
        user=request.user, recipe=recipe).delete()
    return JsonResponse({'success': True})


@login_required
def my_subscriptions(request, username):
    user = get_object_or_404(User, username=username)
    subscriptions = User.objects.prefetch_related('recipe_author').filter(
        following__user=user.id)
    paginator = Paginator(subscriptions, PAGINATOR_ITEMS_ON_THE_PAGE)
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
