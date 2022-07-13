from django.db import models


# Create your models here.

'''
cep         cidade/estado   bairro/distrito     rua                                 complemento (pode ser nulo)
01005010    São Paulo/SP    Sé                  Largo São Francisco
01005020    São Paulo/SP    Sé                  Rua São Francisco
01005030    São Paulo/SP    Sé                  Rua do Ouvidor
01005900    São Paulo/SP    Sé                  Rua Benjamin Constant, 153          Edifício Sinhara
01006000    São Paulo/SP    Sé                  Rua Senador Feijó - lado par
01006001    São Paulo/SP    Sé                  Rua Senador Feijó - lado ímpar
'''

class Ceps():
    cep = models.PositiveIntegerField()
    cidade_estado = models.CharField(max_length=48)
    bairro = models.CharField(max_length=64)