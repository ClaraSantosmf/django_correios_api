from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import ConsultarCep
# from .models import ConsultarCep


# Create your views here.


def index(request):
    return render(request, 'index.html')


def resultado(request):
    cep = request.GET.get('consulta_cep')
    cep = cep.replace('-', '')
    cep = cep.replace('.', '')
    if cep is None or len(cep) != 8:
        return redirect('index')

    endereco = ConsultarCep.objects.filter(cep=cep)

    return render(request, 'resultado.html', {'endereco': endereco})


def consulta_cep(request, cep):

    endereco = ConsultarCep.objects.filter(cep=cep)
    if not endereco:
        resposta = {
            "cep": "invalido"
        }
    else:
        resposta = {
            "cep": cep,
            "rua": endereco[0].rua,
            "bairro": endereco[0].bairro,
            "cidade": endereco[0].cidade,
        }
    return JsonResponse(resposta)
