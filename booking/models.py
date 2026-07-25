from django.db import models
from django.urls import reverse

class Package(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Royal Cinematic Package")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="e.g., 1500.00")
    description = models.TextField(help_text="Brief description of what is included.")
    features = models.TextField(help_text="List features separated by newlines or commas.")
    cover_image = models.ImageField(upload_to='packages/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} (${self.price})"

    def get_features_list(self):
        """Helper to split features into a list for template rendering."""
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class Booking(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    event_date = models.DateField()
    venue = models.CharField(max_length=200)
    selected_package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking by {self.name} for {self.event_date}"