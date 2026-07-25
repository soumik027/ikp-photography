from django.shortcuts import render
from .models import PhotographerProfile, Service, Testimonial
from portfolio.models import WeddingStory
from booking.models import Package

def home_view(request):
    # Explicitly fetch the exact profile entry (e.g., id=1 or order by primary key)
    profile = PhotographerProfile.objects.filter(pk=1).first() or PhotographerProfile.objects.first()
    services = Service.objects.all()
    featured_stories = WeddingStory.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)
    packages = Package.objects.all()[:3] # Display top 3 packages on homepage

    context = {
        'profile': profile,
        'services': services,
        'featured_stories': featured_stories,
        'testimonials': testimonials,
        'packages': packages,
    }
    return render(request, 'home/index.html', context)

def home_view(request):
    profile = PhotographerProfile.objects.first()
    services = Service.objects.all()
    featured_stories = WeddingStory.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)
    packages = Package.objects.all()[:3] # Display top 3 packages on homepage

    context = {
        'profile': profile,
        'services': services,
        'featured_stories': featured_stories,
        'testimonials': testimonials,
        'packages': packages,
    }
    return render(request, 'home/index.html', context)

def about_view(request):
    profile = PhotographerProfile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'home/about.html', context)