import datetime as dt

from django.shortcuts import render

from recipes.models import Cart


# def cart_list_counter(request):
#     """
#     Счётчик рецептов в корзине
#     """
#     if request.user.is_authenticated:
#         count = request.user.carts.all().count()
#     else:
#         count = []
#     return {'count': count}


def year(request):
    today = dt.datetime.today()
    return {'year': today.year}


# def paginator_page(request):
#     """
#     Вставка номера страницы в кнопку пагинатора
#     """
#     result_str = ''
#     for item in request.GET.getlist('pages'):
#         result_str += f'&pages={item}'
#     return {'pages': result_str}
