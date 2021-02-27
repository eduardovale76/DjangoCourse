import pytest
from django.test import Client
from django.urls import reverse

# Emularpip requisições HTTP


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert(resp, '<title>Python Pro</title>')


def test_home_link(resp):
    assert(resp, f'href="{reverse("base:home")}">Python Pro</a>')
