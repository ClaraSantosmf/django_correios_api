from django.db import models

# Create your models here.

class ConsultarCep(models.Model):
    '''
    linhas nos arquivos são finalizadas com o caractere LF (0x0A ou \n)
    campos em cada linha são separados pelo caractere TAB (0x09 ou \t)

    cep         cidade/estado   bairro/distrito     rua                                 complemento
    01005010    São Paulo/SP    Sé                  Largo São Francisco
    01005020    São Paulo/SP    Sé                  Rua São Francisco
    01005030    São Paulo/SP    Sé                  Rua do Ouvidor
    01005900    São Paulo/SP    Sé                  Rua Benjamin Constant, 153          Edifício Sinhara
    01006000    São Paulo/SP    Sé                  Rua Senador Feijó - lado par
    01006001    São Paulo/SP    Sé                  Rua Senador Feijó - lado ímpar
    '''

    cep = models.CharField(max_length=8, unique=True, blank=False, null=False)
    cidade = models.CharField(max_length=64, blank=False, null=False)
    bairro = models.CharField(max_length=64, blank=False, null=False)
    rua = models.CharField(max_length=128, blank=False, null=True)
