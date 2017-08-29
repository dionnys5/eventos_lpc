from django.db import models
from django.contrib.auth.models import User


class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)
    
    def __str__(self):
        return '{} - {}, {}, {}'.format(self.logradouro, self.cidade, self.uf, self.complemento)
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome
    

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)
    mae = models.CharField(max_length=128, null=True)
    pai = models.CharField(max_length=128, null=True)
    
    class Meta:
        verbose_name = 'Pessoa Fisica'
        verbose_name_plural = 'Pessoas Fisicas'

    
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=10)
    ano = models.IntegerField()
    realizador = models.ForeignKey(PessoaFisica, related_name='realizadores', null=True, blank=False)
    endereco = models.ForeignKey(Endereco, related_name='local_evento', null=True, blank=False)
    logo = models.ImageField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

class Inscricao(models.Model):
    participante = models.ForeignKey(PessoaFisica, related_name='participantes', null=True, blank=False)
    festa_evento = models.ForeignKey(Evento, related_name='participantes', null=True, blank=False)
    
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
                           
                           
                           
                           
                           