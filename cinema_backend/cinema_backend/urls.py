# cinema_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.views import vue_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    path('api/auth/', include('movies.urls')),
    path('', vue_app),  # Root URL loads Vue
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

