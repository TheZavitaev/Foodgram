from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from foodgram import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('recipes.urls')),
    # path('', include('social.urls')),

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
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()
