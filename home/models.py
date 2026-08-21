from django.db import models

class PhotographerProfile(models.Model):
    name = models.CharField(max_length=100, default="Indrajeet Karmakar")
    tagline = models.CharField(max_length=200, default="Luxury Wedding & Cinematic Storyteller")
    
    # Journey Section Fields
    subtitle = models.CharField(max_length=100, default="MY JOURNEY")
    title = models.CharField(max_length=200, default="Capturing Emotion & Legacy")
    bio_paragraph_1 = models.TextField(default="Over the last 8 years, I have had the honor of documenting hundreds of weddings across breathtaking destinations. For me, wedding photography is not merely about posing for portraits—it is about capturing the subtle, fleeting moments that tell the true story of your day.")
    bio_paragraph_2 = models.TextField(default="My aesthetic blends editorial fine-art compositions with documentary-style candid storytelling. From quiet intimate exchanges to grand cultural traditions, I ensure every memory is preserved as a timeless masterpiece.")
    
    # Stats Counters
    years_experience = models.CharField(max_length=20, default="8+")
    weddings_shot = models.CharField(max_length=20, default="150+")
    countries = models.CharField(max_length=20, default="12+")

    def __str__(self):
        return self.name