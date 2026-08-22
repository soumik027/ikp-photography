from django.shortcuts import render
from .models import PhotographerProfile
from booking.models import Package

def home_view(request):
    profile = PhotographerProfile.objects.filter(pk=1).first() or PhotographerProfile.objects.first()
    packages = Package.objects.all().order_by('id')[:3]
    context = {
        'profile': profile,
        'packages': packages,
    }
    return render(request, 'home/index.html', context)

def about_view(request):
    profile = PhotographerProfile.objects.filter(pk=1).first() or PhotographerProfile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'home/about.html', context)

def events_view(request):
    return render(request, 'home/events.html')