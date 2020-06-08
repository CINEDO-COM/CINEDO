from django.shortcuts import render
from .models import Genre


def home(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'moviesforyou/genre.html', context)
