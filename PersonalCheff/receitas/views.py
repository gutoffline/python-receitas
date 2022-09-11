from django.shortcuts import render
from .models import Receitas

def index(request):
    receitas = Receitas.objects.all()
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
