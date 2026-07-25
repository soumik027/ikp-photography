from django.db import models

class PhotographerProfile(models.Model):
    name = models.CharField(max_length=100, default="Aarav Sharma")
    tagline = models.CharField(max_length=200, default="Luxury Wedding & Cinematic Storyteller")
    bio = models.TextField(default="Capturing timeless emotions and authentic moments with a cinematic, artistic touch.")
    image = models.ImageField(upload_to='photographer/', blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(default=8)
    weddings_captured = models.PositiveIntegerField(default=250)
    awards_won = models.PositiveIntegerField(default=15)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=250)
    icon_class = models.CharField(max_length=50, default="fas fa-camera-retro", help_text="FontAwesome icon class, e.g., fas fa-camera-retro")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_names = models.CharField(max_length=150, help_text="e.g., Rhea & Vikram")
    wedding_date = models.DateField(blank=True, null=True)
    comment = models.TextField()
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return f"Testimonial by {self.client_names}"