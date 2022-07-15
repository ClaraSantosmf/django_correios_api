from django.contrib import admin
from .models import ConsultarCep

# Register your models here.


class ConsultarCepAdmin(admin.ModelAdmin):

    list_display = ['cep', 'bairro', 'cidade', 'rua']


admin.site.register(ConsultarCep, ConsultarCepAdmin)
