from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="moviesgenre"),
	path('<int:movie_id>', views.movie, name="movie"),
]
