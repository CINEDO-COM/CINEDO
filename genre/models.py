from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/genre', default=False, blank=True, null=True)
    description = models.TextField(blank=True)
    summary = models.TextField(max_length=500)
    def __str__(self):
        return self.name
