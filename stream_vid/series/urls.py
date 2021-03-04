from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'series'

urlpatterns = [
    # /series/
    url(r'^$', views.index, name='index'),

    # /series/search/search_request
    url(r'^search/$', views.search_form, name='search_form'),

    # /series/series_id/slug/
    path('<int:series_id>/<slug:slug>', views.detail, name='detail'),

    # /series/genre/genreName
    url(r'^genre/(?P<genre_id>[a-zA_Z]+)/$', views.series_by_genre, name='series_by_genre'),

    # /series/series_id/series_slug/watch/episode_slug/episode_id0690420
    path('<int:series_id>/<slug:series_slug>/watch/<slug:episode_slug>/<int:episode_id>0690420', views.show_episode, name='show_episode'),

]
