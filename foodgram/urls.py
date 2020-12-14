from django.contrib import admin
from django.contrib.flatpages import views
from django.conf.urls import handler404, handler500
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from foodgram import settings
from social.views import add_favorites, favorites, remove_favorites, \
    my_subscriptions, subscribe, unsubscribe

handler404 = 'recipes.views.page_not_found'  # noqa
handler500 = 'recipes.views.server_error'  # noqa

urlpatterns = [

    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),

    path('', include('recipes.urls')),


# переместить в социал
    path('favorites', add_favorites, name='add_favorites'),
    path('<str:username>/favorites/', favorites, name='favorite'),
    path('favorites/<int:recipe_id>', remove_favorites, name='remove_favorites'),

    path('subscriptions', subscribe, name='subscribe'),
    path('<str:username>/subscriptions/', my_subscriptions, name='my_subscriptions'),
    path('subscriptions/<int:author_id>', unsubscribe, name='unsubscribe'),


    path('admin/', admin.site.urls),

    path('about/', include('django.contrib.flatpages.urls')),
    path(
        'about-project/', views.flatpage,
        {'url': '/about-project/'}, name='about-project'),
    path(
        'about-author/', views.flatpage,
        {'url': '/about-author/'}, name='about-author'),
    path(
        'about-spec/', views.flatpage,
        {'url': '/about-spec/'}, name='about-spec'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()
