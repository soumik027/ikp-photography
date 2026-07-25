from django.db import models

class SiteSettings(models.Model):
    booking_notification_email = models.EmailField(
        default="karmakar.indrajit02@gmail.com", 
        help_text="Email address where new booking/contact inquiries are sent."
    )
    email = models.EmailField(default="contact@weddingportfolio.com")
    phone = models.CharField(max_length=20, default="+1 (555) 234-5678")
    whatsapp_number = models.CharField(max_length=20, default="+15552345678", help_text="Include country code without '+' or spaces for WhatsApp link, e.g., 15552345678")
    facebook_url = models.URLField(default="https://facebook.com")
    instagram_url = models.URLField(default="https://instagram.com")
    youtube_url = models.URLField(default="https://youtube.com", blank=True, null=True, help_text="YouTube channel link")
    
    map_embed_code = models.TextField(default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387193.30596073366!2d-74.25986548373307!3d40.69767006788204!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sin!4v1620000000000!5m2!1sen!2sin", help_text="Google Maps Embed URL")
    address = models.CharField(max_length=250, default="123 Cinematic Studio Way, New York, NY")

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Global Site Contact & Social Settings"