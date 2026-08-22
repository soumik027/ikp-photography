from django.db import models

class SiteSettings(models.Model):
    booking_notification_email = models.EmailField(
        default="karmakar.indrajit02@gmail.com", 
        help_text="Email address where new booking/contact inquiries are sent."
    )
    email = models.EmailField(default="contact@weddingportfolio.com")
    phone = models.CharField(max_length=20, default="+91 90643 08037")
    whatsapp_number = models.CharField(max_length=20, default="9064308037", help_text="Include country code without '+' or spaces for WhatsApp link, e.g., 15552345678")
    facebook_url = models.URLField(default="https://www.facebook.com/share/1Cm3a5YX8T/")
    instagram_url = models.URLField(default="https://www.instagram.com/indrajit_karmakar_official?igsh=MWtpcGh6MDZkdGdiMQ==")
    youtube_url = models.URLField(default="https://www.youtube.com/@indrajitkarmakarofficial8741", blank=True, null=True, help_text="YouTube channel link")
    
    map_embed_code = models.TextField(default="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3675.818343319837!2d87.78128007530965!3d22.883167979271697!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMjLCsDUyJzU5LjQiTiA4N8KwNDcnMDEuOSJF!5e0!3m2!1sen!2sin!4v1784957067266!5m2!1sen!2sin")
    address = models.CharField(max_length=250, default="123 Cinematic Studio Way, New York, NY")

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Global Site Contact & Social Settings"