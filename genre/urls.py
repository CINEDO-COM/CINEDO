from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="moviesforyou"),
	#path('<int:movie_id>', views.movie, name="movie"),
]
