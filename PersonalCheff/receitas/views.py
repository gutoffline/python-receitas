from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'nome_da_receita':'Suco de Laranja'})

def receita(request):
    return render(request, 'receita.html')
