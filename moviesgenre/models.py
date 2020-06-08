from django.db import models
from genre.models import Genre

class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500)
    imagethumb = models.ImageField(upload_to='photos/thumb/', default=False, blank=True, null=True)
    imagefull = models.ImageField(upload_to='photos/full/', default=False, blank=True, null=True)
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    imdburl = models.URLField(max_length=200)
    addtowatchlist = models.BooleanField(default=False)
    trailerurl = models.URLField(max_length=200)
    def __str__(self):
        return '%s | %s' % (self.genre, self.title)
