from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eventos.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','is_staff', 'url')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Pessoa
        fields = '__all__'
    def create(self, data):
        usuario = data.pop('usuario')
        user = User.objects.create(**usuario)
        pessoa = Pessoa.objects.create(usuario=user, **data)
        return pessoa

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
    def create(self, data):
        evento = Evento.objects.create(**data)
        return evento

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
    def create(self, data):
        ticket = Ticket.objects.create(**data)
        return ticket

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'
    def create(self, data):
        inscricao = Inscricao.objects.create(**data)
        return inscricao

