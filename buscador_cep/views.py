from django.shortcuts import render
# from .models import ConsultarCep


# Create your views here.


def index(request):
    cep = 'todo'
    cidade_estado = 'todo'
    bairro = 'todo'
    complemento = 'todo'

    context = {
        'cep': cep,
        'cidade_estado': cidade_estado,
        'bairro': bairro,
        'complemento': complemento}
    
    return render(request, 'index.html', context)
