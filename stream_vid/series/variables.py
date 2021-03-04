from .models import Series, Episode


# tuple of tuples
GENRE_CHOICES = (
        ("action", "Action"), ("adventure", "Adventure"), ("animated", "Animated"),
        ("comedy", "Comedy"), ("crime", "Crime"), ("documentary", "Documentary"),
        ("drama", "Drama"), ("fantasy", "Fantasy"), ("horror", "Horror"), ("kids", "Kids")
    )

# list
genres = [
    "Action", "Adventure", "Animated", "Comedy", "Crime",
    "Documentary", "Drama", "Fantasy", "Horror", "Kids"
]

# dictionary
DICTIONARY = {
    1: "Action", 2: "Adventure", 3: "Animated", 4: "Comedy", 5: "Crime",
    6: "Documentary", 7: "Drama", 8: "Fantasy", 9: "Horror", 10: "Kids"
}

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'gif', 'tiff']
VIDEO_FILE_TYPES = ['avi', 'mp4', 'mkv', '3gp', 'ogg', 'wmv', 'webm', 'flv', 'hdv']
SUBTITLE_FILE_TYPES = ['srt', 'sub', 'sbv', 'ass']


# this returns all the series
series_all = Series.objects.all().order_by('title')

# this returns the last three series, most recently uploaded
series_recent = Series.objects.all().order_by('-id')[:3]

# this returns the last three episodes, most recently uploaded
episode_recent = Episode.objects.all().order_by('-id')[:3]

# this returns the three series with the most recent episodes, most recently uploaded episodes
# not working .. yet
# series_episode_recent = Series.objects.get(pk=episode_recent)


# this returns the Action genre series by groups of 4, the first index is zero
series_action = Series.objects.filter(genre__contains="action")[:4]  # returns series 0 to 3
series_action1 = Series.objects.filter(genre__contains="action")[4:8]  # returns series 4 to 7
series_action2 = Series.objects.filter(genre__contains="action")[8:12]  # returns series 8 to 11

# this returns the Adventure genre series by groups of 4, the first index is zero
series_adventure = Series.objects.filter(genre__contains="adventure")[:4]  # returns series 0 to 3
series_adventure1 = Series.objects.filter(genre__contains="adventure")[4:8]  # returns series 4 to 7
series_adventure2 = Series.objects.filter(genre__contains="adventure")[8:12]  # returns series 8 to 11

# this returns the Animated genre series by groups of 4, the first index is zero
series_animated = Series.objects.filter(genre__contains="animated")[:4]  # returns series 0 to 3
series_animated1 = Series.objects.filter(genre__contains="animated")[4:8]  # returns series 4 to 7
series_animated2 = Series.objects.filter(genre__contains="animated")[8:12]  # returns series 8 to 11


one = 1; two = 2; three = 3; four = 4; five = 5
six = 6; seven = 7; height=8


# dictionary
context_index = {
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

