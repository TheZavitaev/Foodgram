from django.contrib import admin

from .models import FavoriteRecipes, SubscribeToAuthor


@admin.register(FavoriteRecipes)
class FavoriteRecipesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipes',)


@admin.register(SubscribeToAuthor)
class SubscribeToAuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
