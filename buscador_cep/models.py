from django.db import models

# Create your models here.


class Estados():
    '''
    estados:
    1,Acre,AC
    2,Alagoas,AL
    3,Amazonas,AM
    campos:
    id
    nome
    sigla
    '''
    pass


class Cidades():
    '''
    cidades:
    1,Abacate da Pedreira (Macapá),4
    2,Abadia de Goiás,9
    3,Abadia dos Dourados,11

    campos:
    id
    nome
    id_estado
    '''
    pass


class Ceps():
    '''
    ceps:
    01001000, Praça da Sé, - lado ímpar, Sé, 8966, 26
    01001001, Praça da Sé, - lado par, Sé, 8966, 26
    01001010, Rua Filipe de Oliveira, , Sé, 8966, 26

    campos:
    id(cep)
    logradouro/nome
    complemento(deve ser juntado com o campo anterior)
    bairro/distrito
    id_cidade
    id_estado
    '''
    pass
