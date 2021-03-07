from django.shortcuts import render
from django.urls import reverse

class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

        
videos = [
   Video('motivacao', 'Video Aperitivo: Motivação', 'JkGbB0XtH1w'),
   Video('instalacao-windows', 'Instalação Windows', 'ScNNfyq3d_w'),
] 

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})