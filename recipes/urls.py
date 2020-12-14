from django.urls import path, include

from recipes.views import (recipe_view, recipe_edit, recipe_add,
                           recipe_delete, index, profile, ingredients_for_js)


urlpatterns = [
    path('', index, name='index'),
    path('new_recipe/', recipe_add, name='new_recipe'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/<int:recipe_id>/', recipe_view, name='recipe_view'),
    path('<str:username>/<int:recipe_id>/edit/',
         recipe_edit, name='recipe_edit'),
    path('<str:username>/<int:recipe_id>/delete/',
         recipe_delete, name='recipe_delete'),
    path('ingredients', ingredients_for_js, name='ingredients_for_js'),
]