from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="masterclasses"),
	path('<int:masterclass_id>', views.masterclass, name="masterclass"),
    path('tips', views.tips, name="tips"),
]
