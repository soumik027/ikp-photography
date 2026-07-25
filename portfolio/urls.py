from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.stories_list_view, name='stories_list'),
    path('stories/<int:pk>/', views.story_detail_view, name='story_detail'),
]