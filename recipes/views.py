from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from users.models import User
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html', {
        'page': page,
        'paginator': paginator,
        'recipes': recipes,
    })


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(
        Recipe, pk=recipe_id
    )
    if not request.user.is_authenticated:
        return render(
            request,
            'recipes/recipe_detail.html',
            {'recipe': recipe}
        )
    profile = get_object_or_404(
        User,
        username=username
    )
    return render(
        request,
        'recipes/recipe_detail.html',
        {'recipe': recipe, 'profile': profile}
    )
