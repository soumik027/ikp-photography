from django.shortcuts import render, get_object_or_404
from .models import WeddingStory

def stories_list_view(request):
    stories = WeddingStory.objects.all()
    context = {
        'stories': stories,
    }
    return render(request, 'portfolio/stories_list.html', context)

def story_detail_view(request, pk):
    story = get_object_or_404(WeddingStory, pk=pk)
    gallery_images = story.gallery_images.all()
    context = {
        'story': story,
        'gallery_images': gallery_images,
    }
    return render(request, 'portfolio/story_detail.html', context)