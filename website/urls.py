from django.urls import path
from . import views 

urlpatterns = [
	path('', views.home, name="home"),
	path('supcreators.html', views.supcreators, name="supcreators"),
	path('blog.html', views.blog, name="blog"),
	path('blogdetails.html', views.blogdetails, name="blogdetails"),
	path('crowdfunding.html', views.crowdfunding, name="crowdfunding"),
	path('crowddetails.html', views.crowddetails, name="crowddetails"),
	path('movies.html', views.movies, name="movies"),
	path('genre.html', views.genre, name="genre"),
	path('pagedetails.html', views.pagedetails, name="pagedetails"),
	path('pagedetails.html', views.pagedetails, name="pagedetails"),
	path('eshop.html', views.eshop, name="eshop"),
	path('item.html', views.item, name="item"),
]