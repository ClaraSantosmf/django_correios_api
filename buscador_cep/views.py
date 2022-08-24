import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Cep, Cidade, Estado


# Create your views here.


def index(request):
    return render(request, "index.html")


def resultado(request):
    cep = request.GET.get("consulta_cep")
    cep = cep.replace("-", "")
    cep = cep.replace(".", "")
    endereco = {}
    if cep is None or len(cep) != 8:
        return redirect("index")
    try:
        endereco = Cep.objects.get(cep=cep)
    except ObjectDoesNotExist:
        cepinvalido = {"cepinvalido": "Número de CEP inválido 😣"}
        return render(
            request,
            "resultado.html",
            {"endereco": endereco, "cepinvalido": cepinvalido},
        )
    return render(request, "resultado.html", {"endereco": endereco})


def consulta_cep(request, cep):

    endereco = Cep.objects.filter(cep=cep).first()
    if not endereco:
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
        if 'erro' in endereco:
            resposta = {"cep": "invalido"}
        else:
            resposta = {
                "cep": cep,
                "logradouro": endereco['logradouro'],
                "bairro": endereco['bairro'],
                "cidade": endereco['localidade'],
                "estado": endereco['uf'],
                "complemento": endereco['complemento']
            }
        alimentando_o_banco(resposta)
    else:
        resposta = {
            "cep": cep,
            "logradouro": endereco.logradouro,
            "bairro": endereco.bairro,
            "cidade": endereco.cidade.nome,
        }

    return JsonResponse(resposta)

def alimentando_o_banco(resposta):
    if 'estado' in resposta.keys():
        siglaDaResposta = resposta['estado']
        try:
           estadoDaAPI = Estado.objects.get(sigla=siglaDaResposta)
        except:
           estadoDaAPI = Estado.objects.create(nome=resposta['estado'], sigla=resposta['estado'])
            #Isso é um problema, como atribuir de uma sigla o nome de um estado?
    if 'cidade' in resposta.keys():
        cidadeDaResposta = resposta['cidade']
        try:
           cidadeDaAPI = Cidade.objects.get(nome=cidadeDaResposta, estado=estadoDaAPI)
        except:
            cidadeDaAPI = Cidade.objects.create(nome=cidadeDaResposta, estado=estadoDaAPI)
            #Se for criar, como criar associado o estado?
    if 'cep' in resposta.keys():

        cepDaResposta = resposta['cep']
        bairroDaResposta = resposta['bairro']
        complementoDaResposta= resposta['complemento']
        logradouroDaResposta = resposta['logradouro']

        Cep.objects.create(cep=cepDaResposta, logradouro=logradouroDaResposta, complemento=complementoDaResposta, bairro=bairroDaResposta, cidade=cidadeDaAPI)

        #Os casos de cidade e estado estão sendo inserindo com ID? não tenho certeza
