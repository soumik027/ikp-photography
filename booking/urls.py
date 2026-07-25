from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.packages_view, name='packages'),
    path('book/', views.book_event_view, name='book_event'),
    path('book/<int:package_id>/', views.book_event_view, name='book_event_with_package'),
]