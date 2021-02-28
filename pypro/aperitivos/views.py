from django.shortcuts import render

def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'JkGbB0XtH1w'},
        'instalacao-windows': {'titulo': 'Video Aperitivo: Instalação Windows', 'youtube_id': 'ScNNfyq3d_w'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})