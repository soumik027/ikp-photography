from django.shortcuts import render
from .models import PhotographerProfile, Service, Testimonial
from booking.models import Package


def home_view(request):
    # Get photographer profile (fallback to first profile if ID 1 doesn't exist)
    profile = PhotographerProfile.objects.filter(pk=1).first() or PhotographerProfile.objects.first()

    # Fetch homepage data
    services = Service.objects.all()
    testimonials = Testimonial.objects.filter(is_featured=True)
    packages = Package.objects.all().order_by('id')[:3]

    context = {
        'profile': profile,
        'services': services,
        'testimonials': testimonials,
        'packages': packages,
    }

    return render(request, 'home/index.html', context)


def about_view(request):
    profile = PhotographerProfile.objects.filter(pk=1).first() or PhotographerProfile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'home/about.html', context)