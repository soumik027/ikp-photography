from django.contrib import admin
from .models import WeddingStory, StoryImage

class StoryImageInline(admin.TabularInline):
    model = StoryImage
    extra = 3
    fields = ('image', 'caption', 'order')

@admin.register(WeddingStory)
class WeddingStoryAdmin(admin.ModelAdmin):
    list_display = ('couple_names', 'wedding_date', 'venue', 'is_featured')
    list_filter = ('is_featured', 'wedding_date')
    search_fields = ('couple_names', 'venue', 'short_story')
    inlines = [StoryImageInline]
    date_hierarchy = 'wedding_date'

@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ('story', 'caption', 'order')
    list_filter = ('story',)