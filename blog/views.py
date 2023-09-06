import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

# Inclui a classe HttResponse
from django.http import HttpResponse

from blog.models import Post


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

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


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'


def get_all_posts(request):
    posts = list(Post.objects.values('pk', 'body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data = json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    
    return response

def get_post(request, post_id):
    post = Post.objects.filter(
        pk=post_id
    ).values(
        'pk', 'body_text', 'pub_date'
    ).first()
    
    data = {'success': True, 'post': post}
    status = 200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe.'}
        status=404
        
    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
    )

    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem

    return response