from django.shortcuts import get_object_or_404, render
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'moviesgenre/moviesgenre.html', context)

def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context ={
        'movie': movie
    }
    return render(request, 'moviesgenre/movie.html', context)
