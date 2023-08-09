from django.shortcuts import render

# Inclui a classe HttResponse
from django.http import HttpResponse

from blog.models import Post

# Define uma function view chamada index


def index(request):
    # return HttpResponse('Olá Django - index')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})


# DEfine uma function chamada ola
def ola(request):  # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all()  # recupera todos os posts do banco de dados
    context = {'posts_list': posts}  # cria um dicionário com os dado
    # renderiza o template e passa o contexto
    return render(request, 'posts.html', context)
# Create your views here.
