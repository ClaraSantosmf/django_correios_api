from django.db import models

# Create your models here.


class ConsultarCep(models.Model):
    cep = models.CharField(max_length=8, unique=True, blank=False, null=False)
    cidade = models.CharField(max_length=64, blank=False, null=False)
    bairro = models.CharField(max_length=64, blank=False, null=False)
    rua = models.CharField(max_length=128, blank=False, null=True)

    def __str__(self):
        return f'{self.cep}, {self.cidade}, {self.bairro}, {self.rua}'
