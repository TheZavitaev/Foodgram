from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from foodgram import settings
from social.views import (add_favorites, favorites, remove_favorites,
                          my_subscriptions, subscribe, unsubscribe)


handler404 = 'recipes.views.page_not_found'  # noqa
handler500 = 'recipes.views.server_error'  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('', include('recipes.urls')),

    path('favorites', add_favorites, name='add_favorites'),
    path('<str:username>/favorites/', favorites, name='favorite'),
    path('favorites/<int:recipe_id>', remove_favorites, name='remove_favorites'),

    path('subscriptions', subscribe, name='subscribe'),
    path('<str:username>/subscriptions/', my_subscriptions, name='my_subscriptions'),
    path('subscriptions/<int:author_id>', unsubscribe, name='unsubscribe'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()
