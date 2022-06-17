import datetime
import matplotlib
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from matplotlib import pyplot as plt

from .forms import PostForm
from .forms import CadeiraForm
from .forms import ProjectForm
from .forms import TfcForm
from .models import Post
from .models import PontuacaoQuizz
from .models import Cadeira
from .models import Projeto
from .models import Tfc

matplotlib.use('Agg')


# Create your views here.
def home_page_view(request):
    now = datetime.datetime.now()

    context = {'hora': now.hour}
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def new_cadeira_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/newCadeira.html', context)


def editar_cadeira_page_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(pk=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}

    return render(request, 'portfolio/editar_Cadeira.html', context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def new_project_page_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/newProjeto.html', context)


def editar_project_page_view(request, project_id):
    projeto = Projeto.objects.get(pk=project_id)
    form = ProjectForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'projeto_id': project_id}

    return render(request, 'portfolio/editar_Projeto.html', context)


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def newpost_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/newPost.html', context)


def editar_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/editar_blog.html', context)


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')


def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontuacao, reverse=False)
    listaNomes = []
    listapontuacao = []

    for person in pontuacao_sorted:
        listaNomes.append(person.nome)
        listapontuacao.append(person.pontuacao)

    plt.barh(listaNomes, listapontuacao)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')


def pontuacao_quizz(request):
    score = 0
    if request.POST['fav_language'] == 'html':
        score += 1

    if request.POST['cores'] == 'r3':
        score += 1

    return score


def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })


def tfc_page_view(request):
    context = {'tfcs': Tfc.objects.all()}
    return render(request, 'portfolio/tfc.html', context)


def new_tfc_page_view(request):
    form = TfcForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfc'))

    context = {'form': form}

    return render(request, 'portfolio/newTfc.html', context)


def editar_tfc_page_view(request, tfc_id):
    tfc = Tfc.objects.get(pk=tfc_id)
    form = TfcForm(request.POST or None, instance=tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfc'))

    context = {'form': form, 'tfc_id': tfc_id}

    return render(request, 'portfolio/editar_Tfc.html', context)


def web_page_view(request):
    return render(request, 'portfolio/web.html')


def video_page_view(request):
    return render(request,'portfolio/video.html')