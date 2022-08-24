from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from buscador_cep.models import Estado, Cidade, Cep


def test_index(client, db):
    resposta = client.get(reverse('index'))
    assert resposta.status_code == 200


def test_template_index(client, db):
    resposta = client.get(reverse('index'))
    assertTemplateUsed(resposta, 'index.html')


def test_template_resultado(client, db):
    dados = {
        'consulta_cep': '58053110'
    }
    resposta = client.get(
        reverse('resultado'),
        dados
    )
    assertTemplateUsed(resposta, 'resultado.html')


def test_consulta_cep_api_funcionando(client, db):
    estado = Estado.objects.create(nome='Paraiba', sigla='PB')
    cidade = Cidade.objects.create(nome='joao', estado=estado)
    Cep.objects.create(cep='12345678', cidade=cidade)
    resposta = client.get(reverse('API', kwargs={'cep': '12345678'}))
    assert resposta.json() == {'bairro': None, 'cep': '12345678', 'cidade': 'joao', 'rua': None}


def test_consulta_cep_api_nao_funcionando(client, db):
    url = reverse('API', kwargs={'cep': '00000000'})
    resposta = client.get(url)
    assert resposta.json() == {"cep": "invalido"}
