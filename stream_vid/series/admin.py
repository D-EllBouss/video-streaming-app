from django.contrib import admin
from .models import Series, Episode


# Register your models here.


class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "creator", "series_logo", "trailer_url")
    list_filter = ("genre", "creator")
    search_fields = ("title", "creator", "genre")


class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "series")
    list_filter = ("series",)
    search_fields = ("title", "series")


admin.site.register(Series, SeriesAdmin)

admin.site.register(Episode, EpisodeAdmin)
