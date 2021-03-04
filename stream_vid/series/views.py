from .models import Series, Episode
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db.models import Q
from .forms import SeriesForm, EpisodeForm
from django.contrib.auth.decorators import login_required
from .variables import *
from django.core.paginator import Paginator
from account.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    serie = Series.objects.all().order_by("title")
    paginator = Paginator(serie, 4)
    page = request.GET.get('page')
    series = paginator.get_page(page)

    return render(request, 'series/index.html',
                  {'series': series,
                   'series_all': series_all,
                   'series_recent': series_recent,
                   'series_action': series_action,
                   'series_action1': series_action1,
                   'series_action2': series_action2,
                   'series_animated': series_animated,
                   'series_animated1': series_animated1,
                   'series_animated2': series_animated2,
                   'genres': genres,
                   'GENRE_CHOICES': GENRE_CHOICES
                   }
                  )


def detail(request, series_id, slug):

    if request.user.is_authenticated:

        series = get_object_or_404(Series, pk=series_id, slug=slug)

        return render(request, 'series/single.html',
                      {
                          'series': series,
                          'series_all': series_all,
                          'GENRE_CHOICES': GENRE_CHOICES
                      }
                      )
    else:
        return redirect('series:index')


def series_by_genre(request, genre_id):

    series = Series.objects.filter(genre__contains=genre_id).order_by('title')

    query = request.GET.get("search")
    if query:
        series = series_all.filter(
            Q(title__contains=query) |
            Q(creator__contains=query)
        ).distinct()
        return render(request, 'series/series_genre.html',
                      {
                          'series': series,
                          'series_all': series_all,
                          'genre_id': genre_id,
                          'GENRE_CHOICES': GENRE_CHOICES,
                          'series_animated': series_animated,
                          'series_animated1': series_animated1,
                          'series_animated2': series_animated2
                      }
                      )
    else:
        return render(request, 'series/series_genre.html',
                      {
                          'series': series,
                          'series_all': series_all,
                          'genre_id': genre_id,
                          'GENRE_CHOICES': GENRE_CHOICES,
                          'series_animated': series_animated,
                          'series_animated1': series_animated1,
                          'series_animated2': series_animated2
                      }
                      )


def search_form(request):

    query = request.GET.get("search")
    series = Series.objects.filter(
            Q(title__icontains=query)
        ).distinct().order_by('title')

    return render(request, 'series/search.html',
                  {
                      'series': series,
                      'series_all': series_all,
                      'GENRE_CHOICES': GENRE_CHOICES,
                  }
                  )


def show_episode(request, series_id, series_slug, episode_slug, episode_id):

    if request.user.is_authenticated:
        series = get_object_or_404(Series, pk=series_id, slug=series_slug)
        episode = Episode.objects.get(pk=episode_id, slug=episode_slug)

        context = {
            'series': series,
            'episode': episode,
            'series_all': series_all,
            'GENRE_CHOICES': GENRE_CHOICES
                   }

        return render(request, 'series/watch.html', context)
    else:
        return redirect('series:index')


