from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html="<center><h1>OLA Fabio!</h1></center>"
    return HttpResponse(html)