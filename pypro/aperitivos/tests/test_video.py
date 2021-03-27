import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.model import Video
from model_mommy import mommy


@pytest.fixture
def video(db):
    return mommy.make(Video)

@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + 'Video_nao_existente',)))

def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404

def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)

def test_conteudo_video(resp, video):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{video.youtube_id}"')