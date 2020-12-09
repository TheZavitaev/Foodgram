from django.urls import path, include

from recipes import views


urlpatterns = [
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
    path(
        '',
        views.recipe_list,
        name='recipe_list'
    ),
    path(
        '<str:username>/<int:recipe_id>/',
        views.recipe_view,
        name='recipe_view'
    ),
]
