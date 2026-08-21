"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import events_view  # Imports the events view from your home app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('events/', events_view, name='events'),  # Direct mapping for your static events page
    path('booking/', include('booking.urls')),
    path('contact/', include('contact.urls')),
]

# Serve media files properly both in development and production on Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)