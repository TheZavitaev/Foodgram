from django.urls import path, include

from social import views


app_name = 'social'
urlpatterns = [
    # подписки текущего пользователя
    path('follow/', views.follow_index, name='follow_index'),
    # добавление подписки на автора
    path('add_follow/', views.Following.as_view()),
    # удаление подписки
    path('unfollow/<int:author_id>/', views.Following.as_view()),
    # избранное текущего пользователя
    path('favorit/', views.favorite_index, name='favorite_index'),
    # добавление в избранное
    path('add_favorit/', views.Favorites.as_view()),
    # удаление из избранного
    path('unfavorit/<int:recipe_id>/', views.Favorites.as_view()),
]
