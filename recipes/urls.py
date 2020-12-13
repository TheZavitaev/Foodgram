from django.urls import path, include

from recipes.views import (recipe_view, recipe_edit, recipe_add,
                           recipe_delete, index, profile)


urlpatterns = [
    path('', index, name='index'),
    path('new_recipe/', recipe_add, name='new_recipe'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/<int:recipe_id>/', recipe_view, name='recipe_view'),
    path('<str:username>/<int:recipe_id>/edit/',
         recipe_edit, name='recipe_edit'),
    path('<str:username>/<int:recipe_id>/delete/',
         recipe_delete, name='recipe_delete'),
]

# # просмотр рецепта
# path('recipe/<int:recipe_id>/', views.recipe_view, name='recipe'),
# # создание нового рецепта
# path('recipe_new/', views.recipe_new, name='recipe_new'),
# # редактирование рецепта
# path(
#     'recipe_edit/<int:recipe_id>/',
#     views.recipe_edit,
#     name='recipe_edit'
# ),
# # удаление рецепта
# path(
#     'recipe_delete/<int:recipe_id>/',
#     views.recipe_delete,
#     name='recipe_delete'
# ),
# # обработка запроса от js
# path('ingredients/', views.Ingredients.as_view(), name='ingredients'),
# # список покупок
# path('cart_list/', views.cart_list, name='cart_list'),
# # скачать список покупок
# path(
#     'cart_list/download/',
#     views.cart_list_download,
#     name='cart_list_download'
# ),
# # удаление рецепта из списка покупок
# path(
#     'cart_list/delete/<int:recipe_id>/',
#     views.cart_delete_recipe,
#     name='cart_delete_recipe'
# ),
# # добавление в список покупок. запрос от js
# path('purchases/', views.Purchases.as_view(), name='add_to_cart'),
# # удаление из списка покупок
# path(
#     'purchases/<int:recipe_id>/',
#     views.Purchases.as_view(),
#     name='remove_from_cart'
# ),
# # рецепты пользователя
# path('<str:username>/', views.profile, name='profile'),
# главная страница
