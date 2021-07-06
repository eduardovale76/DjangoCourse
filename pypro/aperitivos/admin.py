from django.contrib.admin import ModelAdmin, register
from pypro.aperitivos.model import Video

@register(Video)
class VideoAdmin(ModelAdmin):
    pass