from django.contrib import admin
from .models import PhotographerProfile

# Customizing Admin Header Titles
admin.site.site_header = "Indrajeet Karmakar Administration"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Luxury Dashboard"

# Shared Luxury CSS injection mixin for all model admins
class LuxuryAdminCssMixin:
    class Media:
        css = {
            'all': ('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Montserrat:wght@300;400;500&display=swap',)
        }
        js = ()

@admin.register(PhotographerProfile)
class PhotographerProfileAdmin(admin.ModelAdmin, LuxuryAdminCssMixin):
    list_display = ('name', 'tagline', 'years_experience', 'weddings_shot', 'countries')
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

    def has_add_permission(self, request):
        count = self.model.objects.count()
        if count >= 1 and not request.resolver_match.url_name.endswith('_change'):
            return False
        return super().has_add_permission(request)