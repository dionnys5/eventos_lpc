from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agenda.models import Agenda, Evento, Usuario

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome',)

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    criador = UsuarioSerializer(many=False)
    class Meta:
        model = Agenda
        fields = ('criador', 'nome','local','descricao','institucional','tipo')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome','dataInicio','dataFim', 'descricao','agenda')
