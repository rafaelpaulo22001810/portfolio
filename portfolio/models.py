from django.db import models


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    conteudo = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:20]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nome


class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField()
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
    projetos = models.ManyToManyField(Projeto)
    imagem = models.ImageField(blank=True, upload_to='portfolio\static\portfolio\images\img_licen')

    def __str__(self):
        return self.nome
