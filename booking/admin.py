from django.contrib import admin
from .models import Package, Booking

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'order')
    list_editable = ('price', 'order')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'event_date', 'selected_package', 'is_confirmed', 'created_at')
    list_filter = ('is_confirmed', 'event_date', 'selected_package')
    search_fields = ('name', 'email', 'phone', 'venue', 'message')
    list_editable = ('is_confirmed',)
    date_hierarchy = 'event_date'
    