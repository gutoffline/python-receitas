from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receitas

def index(request):
    receitas = Receitas.objects.all()
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_exibir = {
        'receita' : receita
    }
    return render(request, 'receita.html', receita_exibir)
