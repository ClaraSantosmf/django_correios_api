from django.shortcuts import render
from .models import ConsultarCep
# from .models import ConsultarCep


# Create your views here.


def index(request):

    return render(request, 'index.html')


def resultado(request):
    cep = request.GET.get('consulta_cep')
    endereco = ConsultarCep.objects.filter(cep=cep)
    return render(request, 'resultado.html', {'endereco': endereco})
