from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('booking_notification_email', 'email', 'phone', 'whatsapp_number')

    def has_add_permission(self, request):
        # Restrict to only 1 global site settings instance
        count = self.model.objects.count()
        if count >= 1 and not request.resolver_match.url_name.endswith('_change'):
            return False
        return super().has_add_permission(request)