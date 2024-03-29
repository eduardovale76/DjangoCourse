from django.db import models
from django.urls import reverse

class Video(models.Model):
    slug = models.CharField(max_length=30)
    titulo = models.CharField(max_length=32)
    youtube_id = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_created=True)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))