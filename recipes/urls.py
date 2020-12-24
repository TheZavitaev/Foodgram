from django.urls import path

from recipes.views import (recipe_view, recipe_edit, recipe_add,
                           recipe_delete, index, profile,
                           PurchaseView, delete_purchase,
                           ingredients_for_js, download_shop_list_txt)

urlpatterns = [
    path('new_recipe/', recipe_add, name='new_recipe'),
    path('<str:username>/<int:recipe_id>/edit/',
         recipe_edit, name='recipe_edit'),
    path('<str:username>/<int:recipe_id>/delete/',
         recipe_delete, name='recipe_delete'),

    path('ingredients', ingredients_for_js, name='ingredients_for_js'),

    path('purchases', PurchaseView.as_view(), name='purchases'),
    path('purchases/<int:recipe_id>', delete_purchase, name='delete_purchase'),
    # path('purchases/download_pdf/',
    #      download_shop_list, name='download_shop_list'),
    path('purchases/download_txt/',
         download_shop_list_txt, name='download_shop_list_txt'),

    path('', index, name='index'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/<int:recipe_id>/', recipe_view, name='recipe_view'),
]
