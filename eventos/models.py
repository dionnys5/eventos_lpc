from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    idade = models.CharField(max_length=3)
    cpf = models.CharField(max_length=11)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=10)
    ano = models.IntegerField()
    realizador = models.ForeignKey(Pessoa, related_name='realizadores', null=True, blank=False)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    
    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class Ticket(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.CharField(max_length=128)
    preco = models.FloatField()
    evento = models.ForeignKey(Evento, null=True, blank=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

class Inscricao(models.Model):
    participante = models.ForeignKey(Pessoa, related_name='participantes', null=True, blank=False)
    ticket = models.ForeignKey(Ticket, null=True, blank=False)
    status = models.BooleanField()
    
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
                           
                           
                           
