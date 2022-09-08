from django.db import models
from datetime import datetime

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    nota = models.IntegerField()
    dificuldade = models.IntegerField()
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
