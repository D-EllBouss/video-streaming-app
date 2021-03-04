from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission
from django.urls import reverse, reverse_lazy
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField
from django.core.validators import URLValidator


# Create your models here.


class Series(models.Model):
    GENRE_CHOICES = (
        ("action", "Action"), ("adventure", "Adventure"), ("animated", "Animated"),
        ("comedy", "Comedy"), ("crime", "Crime"), ("documentary", "Documentary"),
        ("drama", "Drama"), ("fantasy", "Fantasy"), ("horror", "Horror"), ("kids", "Kids")
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    creator = models.CharField(max_length=250, null=True, blank=True)
    genre = MultiSelectField(choices=GENRE_CHOICES, max_choices=6, max_length=100)
    series_logo = models.ImageField(upload_to='images/', null=False, blank=False)
    trailer_url = models.TextField(validators=[URLValidator()], null=True, blank=True)
    description = models.CharField(max_length=2000)

    def get_absolute_url(self):
        return reverse('series:detail', args=[self.pk, self.slug])

    def __str__(self):
        return self.title + ' - ' + self.creator


class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=280)
    video_file_url = models.TextField(validators=[URLValidator()])

    def get_absolute_url(self):
        return reverse('series:episode', args=[self.pk, self.slug])

    def __str__(self):
        return str(self.series) + ": " + self.title

