from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('moviesgenre/', include('moviesgenre.urls')),
    path('moviesforyou/', include('genre.urls')),
    path('masterclasses/', include('masterclasses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
