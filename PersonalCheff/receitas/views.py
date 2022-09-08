from django.shortcuts import render

def index(request):
    receitas = {
        1:'Suco de Laranja',
        2:'Suco de Limão',
        3:'Suco de Morango'
    }
    
    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
