import pytest
from django.test import Client
from django.urls import reverse
from pypro.django_assertions import assert_contains

# Emularpip requisições HTTP


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')

def test_email_link(resp):
    assert_contains(resp, 'href="mailto:teste@teste.com"')