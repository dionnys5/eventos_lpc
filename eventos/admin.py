from django.contrib import admin

# Register your models here.

from eventos.models import Pessoa, PessoaFisica, Evento, Inscricao
admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Inscricao)
