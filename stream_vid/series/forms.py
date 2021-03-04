from django import forms
from django.contrib.auth.models import User
from .models import Series, Episode


class SeriesForm(forms.ModelForm):

    class Meta:
        model = Series
        fields = ['creator', 'title', "slug", 'genre', 'series_logo', 'description', 'trailer_url']


class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episode
        fields = ["title", "slug", "video_file_url"]
