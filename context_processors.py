from contact.models import SiteSettings

def site_settings_processor(request):
    try:
        settings = SiteSettings.objects.first()
    except Exception:
        settings = None
    return {
        'site_settings': settings
    }