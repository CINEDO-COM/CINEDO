from django.db import models

class Masterclass(models.Model):
    title = models.CharField(max_length=100)
    imagethumb = models.ImageField(upload_to='photos/thumb/', default=False, blank=True, null=True)
    imagefull = models.ImageField(upload_to='photos/full/', default=False, blank=True, null=True)
    description = models.TextField(blank=True)
    summary = models.TextField(max_length=500)
    unit1 = models.TextField(max_length=200, default=False, blank=True, null=True)
    unit2 = models.TextField(max_length=200, default=False, blank=True, null=True)
    unit3 = models.TextField(max_length=200, default=False, blank=True, null=True)
    book1 = models.TextField(max_length=200, default=False, blank=True, null=True)
    bookurl1 = models.URLField(max_length=200, default=False, blank=True, null=True)
    book2 = models.TextField(max_length=200, default=False, blank=True, null=True)
    bookurl2 = models.URLField(max_length=200, default=False, blank=True, null=True)
    book3 = models.TextField(max_length=200, default=False, blank=True, null=True)
    bookurl3 = models.URLField(max_length=200, default=False, blank=True, null=True)
    quiz = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    def __str__(self):
        return self.title
