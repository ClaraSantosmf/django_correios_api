from builtins import Exception

from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Cep


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
    except Exception:
        cepinvalido = {"cepinvalido": "Número de CEP inválido 😣"}
        return render(
            request,
            "resultado.html",
            {"endereco": endereco, "cepinvalido": cepinvalido},
        )
    return render(request, "resultado.html", {"endereco": endereco})


def consulta_cep(request, cep):
    endereco = Cep.objects.get(cep=cep)
    if not endereco:
        resposta = {"cep": "invalido"}
    else:
        resposta = {
            "cep": cep,
            "rua": endereco.logradouro,
            "bairro": endereco.bairro,
            "cidade": endereco.cidade.nome,
        }
    return JsonResponse(resposta)
