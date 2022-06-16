from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    conteudo = models.TextField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:20]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField()

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
    imagem = models.ImageField(blank=True, upload_to='portfolio\static\portfolio\images\img_proj')

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField(default=0)
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE, default='')
    docente_pratica = models.ForeignKey(Professor, related_name='caderias', on_delete=models.CASCADE, default='')
    projetos = models.ForeignKey(Projeto, on_delete=models.CASCADE, default='')
    classificacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    imagem = models.ImageField(blank=True, upload_to='portfolio\static\portfolio\images\img_licen')

    def __str__(self):
        return self.nome


class Tfc(models.Model):
    autor = models.CharField(max_length=200)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(blank=True, upload_to='portfolio\static\portfolio\images\img_tfc')
    relatorio = models.CharField(max_length=1000)
    github = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo[:70]