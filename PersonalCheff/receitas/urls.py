# para poder utilizar as urls do django precisamos importar as urls
from django.urls import path

# o arquivo de views é quem faz a manipulação de qual url será devolvida e exibida 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('receita/<int:receita_id>/',views.receita, name='receita')
    
]