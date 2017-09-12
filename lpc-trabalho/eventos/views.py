from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import *

html='<html lang=pt> <head>'
html=html+'<meta charset="utf-8">'
html=html+'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
html=html+'<meta name="description" content="Django para LPC">'
html=html+'<meta name="author" content="Joao Antonio Santos">'
html=html+'<link rel="icon" href="http://joaoantoniosantos.com.br/img/favicon.png">'
html=html+'<title>LPC</title>'
html=html+'<link href="http://joaoantoniosantos.com.br/css/bootstrap.min.css" rel="stylesheet"><link href="http://joaoantoniosantos.com.br/navbar-top-fixed.css" rel="stylesheet">'
html=html+'<link href="http://joaoantoniosantos.com.br/css/docs.min.css" rel="stylesheet">'
html=html+'<link href="http://joaoantoniosantos.com.br/cover.css" rel="stylesheet">'
html=html+'</head><body>'
html=html+'<nav class="navbar">'
html=html+'<ul class="navbar-nav">'
html=html+'<li class="nav-item">Gerenciador de Eventos</li>'
html=html+'<li class="nav-item"><a class="nav-link" href="http://localhost:8000/">Inicio</a></li>'
html=html+'<li class="nav-item"><a class="nav-link" href="http://localhost:8000/eventos/">Eventos</a></li>'
html=html+'<li class="nav-item"><a class="nav-link" href="http://localhost:8000/admin/">Admin</a></li></ul>'
html=html+'</nav>'
html=html+'<div class="site-wrapper"><div class="cover-container"><div class="inner cover">'
html=html+'<p class="lead">'
# Create your views here.
html1=''
html1=html1+'</p></div></div></div>'
html1=html1+'<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>'
html1=html1+'<script>window.jQuery || document.write("<script src="http://joaoantoniosantos.com.br/js/jquery.min.js"><\/script>"")</script>'
html1=html1+'<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>'
html1=html1+'<script src="http://joaoantoniosantos.com.br/js/bootstrap.min.js"></script>'
html1=html1+'<script src="http://joaoantoniosantos.com.br/js/ie10-viewport-bug-workaround.js"></script>'
html1=html1+'</body></html>'
html1=html1+''
def index(request):
    final=''
    final+=final+html+''+html1
    return HttpResponse(final)

def listaEvento(request):
    final=''
    retorno = '<h1>Eventos: </h1><br>'
    lista = Evento.objects.all()
    final=final+html
    for evento in lista:
        retorno+='<div class="card" style="color:black !important;"><div class="card-block"><h4 class="card-title">{} - {}</h4>'.format(evento.sigla, evento.nome)
        retorno+='<h6 class="card-subtitle mb-2 text-muted">{}</h6>'.format(evento.eventoPrincipal)
        retorno+='<p class="card-text">Data e Hora de Inicio: {} <br>Realizador: {}</p>'.format(evento.dataEHoraDeInicio, evento.realizador)
        retorno+='<p class="card-text">Endereco: {} - {} - {} - Cep: {}</p>'.format(evento.endereco,evento.cidade,evento.uf,evento.cep)
        retorno+='</div></div>'
    final=final+retorno+html1
    return HttpResponse(final)
def get_evento_byID(request,id):
    final=''
    retorno = '<h1>Eventos: </h1><br>'
    evento = Evento.objects.get(pk=id)
    final=final+html
    retorno+='<div class="card" style="color:black !important;"><div class="card-block"><h4 class="card-title">{} - {}</h4>'.format(evento.sigla, evento.nome)
    retorno+='<h6 class="card-subtitle mb-2 text-muted">{}</h6>'.format(evento.eventoPrincipal)
    retorno+='<p class="card-text">Data e Hora de Inicio: {} <br>Realizador: {}</p>'.format(evento.dataEHoraDeInicio, evento.realizador)
    retorno+='<p class="card-text">Endereco: {} - {} - {} - Cep: {}</p>'.format(evento.endereco,evento.cidade,evento.uf,evento.cep)
    retorno+='</div></div>'
    final=final+retorno+html1
    return HttpResponse(final)