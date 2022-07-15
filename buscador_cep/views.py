from django.shortcuts import render
from .models import ConsultarCep
# from .models import ConsultarCep


# Create your views here.


def index(request):
    return render(request, 'index.html')


def resultado(request):
    cep = ConsultarCep.objects.get(id=84)
    cidade = 'todo'
    bairro = 'todo'
    rua = 'todo'

    context = {
        'cep': cep,
        'cidade': cidade,
        'bairro': bairro,
        'rua': rua,
    }

    return render(request, 'resultado.html', context)
