from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path, include

urlpatterns = [
    # админка и авторизация
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),

    # # flatpages
    # path('about/', include('django.contrib.flatpages.urls')),
    # path(
    #     'about-project/', views.flatpage,
    #     {'url': '/about-project/'}, name='about-project'),
    # path(
    #     'about-author/', views.flatpage,
    #     {'url': '/about-author/'}, name='about-author'),
    # path(
    #     'about-spec/', views.flatpage,
    #     {'url': '/about-spec/'}, name='about-spec'),

    # подключаем urls приложений
    path('', include('social.urls')),
    path('', include('recipes.urls')),
]
