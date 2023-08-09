from django.shortcuts import render

#Inclui a classe HttResponse
from django.http import HttpResponse



#Define uma function view chamada index
def index(request):
    #return HttpResponse('Olá Django - index')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})



#DEfine uma function chamada ola
def ola(request):
    #return HttpResponse('Ola Django')
    return render(request, 'home.html')
# Create your views here.



