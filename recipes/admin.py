from django.contrib import admin
from django.db.models import Count

from .models import Recipe, Ingredient, Tag, IngredientAmount, Cart


class IngredientAmountInline(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline, )
    list_display = (
        'id', 'title', 'author',
        'image', 'cooking_time',
    )
    list_filter = ('author', )
    search_fields = ('title', 'author__username', )
    autocomplete_fields = ('author', )
    ordering = ('-pub_date', )

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     return queryset.annotate(_get_favorite=Count('recipe_favorite'))
    #
    # def get_tag(self, obj):
    #     return list(obj.recipe_tag.values_list('title', flat=True))
    #
    # def get_favorite(self, obj):
    #     return obj._get_favorite
    #
    # get_tag.short_description = 'теги'
    # get_favorite.short_description = 'добавлен в избранное, раз'
    # get_favorite.admin_order_field = '_get_favorite'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'measure', )
    search_fields = ('^title', )


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'shopper',)
