from django.shortcuts import render
from .models import SiteSettings

def contact_view(request):
    settings = SiteSettings.objects.first()
    context = {
        'settings': settings,
    }
    return render(request, 'contact/contact.html', context)