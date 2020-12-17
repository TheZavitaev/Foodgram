from django.contrib import admin
from django.db.models import Count

from .models import Recipe, Ingredient, Tag, IngredientValue, Purchase


class IngredientValueInline(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientValueInline, )
    list_display = (
        'id', 'title', 'author',
        'image', 'cooking_time',
    )
    list_filter = ('author', )
    search_fields = ('title', 'author__username', )
    autocomplete_fields = ('author', )
    ordering = ('-pub_date', )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dimension', )
    search_fields = ('^title', )


@admin.register(IngredientValue)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'value', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', )
