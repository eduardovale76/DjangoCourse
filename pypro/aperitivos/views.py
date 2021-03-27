from django.db.models.fields import SlugField
from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.model import Video


videos = [
   Video(slug='motivacao', titulo='Video Aperitivo: Motivação', youtube_id='JkGbB0XtH1w'),
   Video(slug='instalacao-windows', titulo='Instalação Windows', youtube_id='ScNNfyq3d_w'),
] 

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})