from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("movies/", views.home, name="home"),
    path('movie_upload/', views.movie_view, name='movie_upload'),
    path('actor-autocomplete/', views.actor_autocomplete, name='actor_autocomplete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)