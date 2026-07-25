from django.db import models
from django.urls import reverse

class WeddingStory(models.Model):
    couple_names = models.CharField(max_length=150, help_text="e.g., Ananya & Rohan")
    wedding_date = models.DateField()
    venue = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='portfolio/covers/', help_text="Main cover image for cards and banner")
    short_story = models.TextField(help_text="A brief summary description of the wedding day.")
    full_story = models.TextField(blank=True, null=True, help_text="Detailed narrative of the wedding celebration.")
    is_featured = models.BooleanField(default=False, help_text="Display on homepage featured section")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-wedding_date']
        verbose_name_plural = "Wedding Stories"

    def __str__(self):
        return f"{self.couple_names} - {self.venue}"

    def get_absolute_url(self):
        return reverse('story_detail', kwargs={'pk': self.pk})

class StoryImage(models.Model):
    story = models.ForeignKey(WeddingStory, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Gallery image for {self.story.couple_names} ({self.id})"