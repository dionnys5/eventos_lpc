from django.contrib import admin

# Register your models here.

from eventos.models import Evento, Inscricao, Ticket

admin.site.register(Ticket)
admin.site.register(Evento)
admin.site.register(Inscricao)
