from django.shortcuts import render

def indice(request):
    return render(request, 'aperitivos/indice.html')


def video(request, slug):
    videos = {
        'motivacao': {'titulo': '', 'youtube_id': 'JkGbB0XtH1w'},
        'instalacao-windows': {'titulo': 'Video Aperitivo: Instalação Windows', 'youtube_id': 'ScNNfyq3d_w'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})