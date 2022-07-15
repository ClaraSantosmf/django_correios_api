from django.shortcuts import redirect, render
from .models import ConsultarCep
# from .models import ConsultarCep


# Create your views here.


def index(request):
    return render(request, 'index.html')


def resultado(request):
    cep = request.GET.get('consulta_cep')
    if len(cep) == 8 and cep is not None:
        endereco = ConsultarCep.objects.filter(cep=cep)
        return render(request, 'resultado.html', {'endereco': endereco})

    else:
        return redirect('index')
