from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/recipes_list.html', {
        'page': page,
        'paginator': paginator,
        'recipe': recipes,
    })
