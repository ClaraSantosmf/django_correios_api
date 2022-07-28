from django.test import TestCase
from django.urls import reverse

# Create your tests here.

def test_index(client, db):
    resposta = client.get(reverse('index'))
    assert resposta.status_code == 200

