from django.db import models
import datetime

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.cpf)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=128)
    razao_social = models.CharField(max_length=128)
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.cnpj)
class Autor(Pessoa):
    curriculo = models.CharField(max_length=128)
    artigos = models.ManyToManyField('ArtigoCientifico')

    def __str__(self):
        return '{} - {}'.format(self.nome, self.curriculo)

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=128, null=True, blank=False)
    sigla = models.CharField(max_length=128, null=True, blank=False)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=128, null=True, blank=False)
    logoTipo = models.CharField(max_length=128, null=True, blank=False)
    realizador = models.ForeignKey(Pessoa, null=True, blank=False)
    cidade = models.CharField(max_length=128)
    uf = models.CharField(max_length=128)
    endereco = models.CharField(max_length=128, null=True, blank=False)
    cep = models.CharField(max_length=128, null=True, blank=False)
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.dataEHoraDeInicio)

class EventoCientifico(Evento):
    issn = models.CharField(max_length=128)
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.issn)

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=128)
    autores = models.ManyToManyField('Autor')
    evento = models.ForeignKey(EventoCientifico, null=True, blank=False)
    
    def __str__(self):
        return '{} - {}'.format(self.titulo, self.evento)