from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eventos.models import Evento, Ticket, Inscricao

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    realizador = UserSerializer(many = False)
    class Meta:
        model = Evento
        fields = '__all__'

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many = False)
    class Meta:
        model = Ticket
        fields = '__all__'

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    participante = UserSerializer(many = False)
    festa_evento = EventoSerializer(many = False)
    ticket = TicketSerializer(many = False)
    class Meta:
        model = Inscricao
        fields = '__all__'

