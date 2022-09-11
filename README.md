# PersonalCheff

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<img src="exemplo-image.png" alt="exemplo imagem">

> Uma aplicação web de receitas culinárias chamada PersonalCheff que receberá novas receitas de culinária utilizando Python e o framework de Django. Clicando em cada ícone, serão apresentadas as informações, ingredientes e modo de preparo.

### Lista de tarefas

Segue a lista de tarefas a serem desenvolvidas no projeto:

- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
- [X] Criar e ativar o ambiente virtual
    ```python
    # utilizar python ou python3
    python3 -m venv .\venv\ 
    venv\Scripts\activate
    # se der erro no powershell utilize o comando abaixo para resolver a permissão
    # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
- [X] Instalar o Django
    ```python
    # utilizar a versão 3.2 pois é a LTS
    python -m pip install django==3.2
    ```
- [X] Criar o projeto PersonalCheff
    ```python
    # substituir o nome PersonalCheff pelo nome do projeto que você quiser
    django-admin.py startproject PersonalCheff
    ```
- [X] Subir o servidor e testar o projeto
    ```python
    cd PersonalCheff
    python manage.py runserver
    ```
- [X] Alterar o idioma da aplicação para pt-br
    - No arquivo `settings.py` alterar na linha 106 de `en-us` para `pt-br`
- [X] Alterar o time zone da aplicação para são paulo
    - No arquivo `settings.py` alterar na linha 106 de `UTC` para `America/Sao_Paulo`
    - lista de time zones [aqui](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)
- [X] Criar app receitas
    ```python
    python manage.py startapp receitas
    ```
- [X] Registrar o app receitas
    - Em `apps.py`, visualizamos a classe `ReceitasConfig()` com um `name` que deve ser igual a `receitas` que é utilizado para seu registro, dizendo às configurações de que esse app criado faz parte do projeto.
    - Em `settings.py`, adicionamos 'receitas' à lista de apps (INSTALLED_APPS). Ao salvar, este está registrado no trabalho. 
- [X] Configurando a rota inicial
    - Dentro da pasta receitas(app) criar o arquivo `urls.py`
    - no arquivo  `urls.py`
        ```python
        # para poder utilizar as urls do django precisamos importar as urls
        from django.urls import path

        # o arquivo de views é quem faz a manipulação de qual url será devolvida e exibida 
        from . import views

        urlpatterns = [
            # path(rota, view, namespace)
            path('',views.index, name='index')
        ]
        ```
- [X] Criando a view para a rota inicial
    - Dentro da pasta receitas(app) abrir o arquivo `views.py`
        ```python
        from django.shortcuts import render
        from django.http import HttpResponse

        def index(request):
            return HttpResponse('<h1>PersonalCheff</h1>')
        ```
- [X] Registrando a rota inicial
    - Dentro da pasta PersonalCheff(app) abrir o arquivo `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('', include('receitas.urls')),
            path('admin/', admin.site.urls),
        ]
        ```
- [X] Criando o arquivo index.html
    - Dentro de receitas crie a pasta `templates` 
    - Dentro da pasta templates crie o arquivo `index.html`. Neste arquivo crie seu index como desejar.
    - No arquivo `views.py` faça as alterações:
        ```python
        from django.shortcuts import render

        def index(request):
            return render(request, 'index.html')
        ```
- [X] Integrar arquivos estáticos (CSS, JS)
    - https://docs.djangoproject.com/pt-br/2.0/howto/static-files/
    - no arquivo `settings.py`:
        - importe a bibliotec os utilizando `import os`no início do arquivo
        - na linha 58 adicionar valor à propriedade `DIRS` da seguinte forma:
            ```python
            'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],
            ```
        - no final do arquivo, após a linha `STATIC_URL` adicionar as linhas abaixo para referenciar ao django aonde estão nossos arquivos estáticos:
            ```python
            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'PersonalCheff/static')
            ]
            ```
        - dentro da pasta do projeto PersonalCheff crie uma pasta chamada `static` e coloque seus arquivos estáticos (img, css, js)
        - no terminal(dentro da pasta do projeto) digite `python manage.py collectstatic`
        - no arquivo index.html  coloque o comando python `{% load static %}`
        - agora, nos arquivos html, quando for carregar algum arquivo estático  você deve utilizar como no exemplo abaixo:
            ```python
            <img src="{% static 'logo.png' %}">
            ```
- [X] Utilizando links
    - para criar um link para a página index ou outra rota qualquer você deve utilizar:
        ```python
        <a href="{% url 'index' %}">Home</a>
        ```
- [X] Criando o base.html
    - na pasta templates crie o arquivo `base.html`. Esse arquivo será o código base de todas as páginas para evitar duplicação de código. Nele você deve deixar tudo que tiver antes do `<body>` e tudo que tiver depois do `</body>`.
    - no arquivo `base.html`, no local onde deve ser carregado o conteúdo das outras páginas, ou seja o conteúdo diferente você deve utilizar o comando `{% block content %}` e `{% endblock%}` 
    - nesse arquivo deve ter o `{% load static %}` para carregar os arquivos estáticos
    - o código do arquivo `base.html` deve ser algo como:
        ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="pt-br">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PersonalCheff</title>
        </head>

        <body>
            {% block content %}

            {% endblock %}
        </body>

        </html>
        ```
    - no arquivo aonde será utilizado o base.html (o index, o receita, etc) você deve iniciar com a instrução `{% extends 'base.html' %}` e indicar o início e fim do do bloco com os respectivos comandos `{% block content %}` e `{% endblock %}`.
    - o `index.html` ficará parecido com:
        ```html
        {% extends 'base.html' %}
        {% load static %}
        {% block content %}
        <a href="{% url 'index' %}">
            <img src="{% static 'logo.png' %}">
        </a>
        <h1>PersonalCheff</h1>
        <h2>Seja bem vindo ao site</h2>
        <table>
            .
            .
            .
        </table>
        {% endblock %}
        ```
- [X] Separando em partials
    - dentro da pasta templates crie uma pasta chamada `partials`
    - dentro da pasta partials crie os arquivos que serão as partes utilizadas como `header.html`, `footer.html`, `menu.html`, etc.
    - insira dentro dos arquivos os respectivos códigos das partes. Não se esqueça de utilizar o comando `{% load static %}` para carregar os arquivos estáticos
    - para incluir as partials nos arquivos de destino utilize `{% include 'partials/header.html' %}`  no local onde deseja inserir.
- [X] Renderizando dados dinamicamente
    - Vamos trocar as informações da receita que no momento estão com dados fixos para dados dinâmicos. Eu quero gerar a lista de receitas de forma dinâmica, para isso existe uma forma de fazer isso usando o Django passando uma informação para o `template`, na hora que vou renderizar a página `index.html`. Vamos no arquivo `views.py` e passar um dicionário na linha aonde realizamos a rederização do `index.html`:
        ```python
        def index(request):
            return render(request, 'index.html', {'nome_da_receita':'Suco de Laranja'})
        ```
    - Agora precisamos informar no nosso template aonde será exibida a informação do dicionário passado. Vá no arquivo `index.html` e vamos utilizar os marcadores `{{ }}` ao invés de `{% %}`. Utilizando o delimitador `{% %}` consigo incluir qualquer código python no meu template html. Este código será processado mas não necessariamente será impresso na tela. Só se eu fizer um `print(nome)`, que o valor do nome vai aparecer. Utilizamos o delimitador `{{ }}` para imprimir texto no html. Resumindo:
        - `{{ }}` é utilizado apenas para chamar variáveis. Já o `{% %}` é utilizado para utilizar os métodos do python, como `if` e `for`.
    - no arquivo `index.html` substitua o texto `SUCO DE LARANJA` por `{{ nome_da_receita }}` :
        ```html
        <td><a href="{% url 'receita' %}">{{nome_da_receita}}</a></td>
        ```
- [X] Criando um dicionario com as receitas
    - no arquivo `views.py` vamos criar um dicionário com as receitas, modifique a função index da seguinte forma: 
        ```python
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
        ```
    - na página `index.html` precisamos criar um laço de repetição para listar as receitas. Para isso vamos pegar a linha da tabela e colocar dentro de um laço que leia a quantidade de receitas: 
        ```python
        <tbody>
            {% for chave, nome_da_receita in nome_das_receitas.items %}
                <tr>
                    <td><a href="{% url 'receita' %}">{{nome_da_receita}}</a></td>
                    <td>https://www.youtube.com/watch?v=Nn9140bDPnc</td>
                </tr>
            {% endfor %}
        </tbody>
        ```
- [X] Criando o banco de dados(MySQL/MariaDB)
    - No terminal, execute o comando `pip install mysqlclient` para instalar a lib do mysql
    - Abra o PHPMyAdmin e crie um banco de dados chamado `dbreceitas`
- [X] Instalando o conector do bando de dados MySQL
    - Abra o arquivo `settings.py` e vá até a linha de configuração `DATABASES` (~78) e realize a configuração de acesso ao banco de dados da seguinte forma:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'dbreceitas',
                'USER': 'root',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```
- [X] Criando o modelo da receita
    - abra o arquivo `models.py` que está dentro da pasta receitas (app). Vamos criar o nosso modelo para receitas:
        ```python
        from django.db import models
        from datetime import datetime

        class Receitas(models.Model):
            nome_receita = models.CharField(max_length=100)
            ingredientes = models.TextField()
            modo_preparo = models.TextField()
            nota = models.IntegerField()
            dificuldade = models.IntegerField()
            data_receita = models.DateTimeField(default=datetime.now, blank=True)
        ```
- [X] Criando a migration (mapeamento)
    - no terminal digite o comando `python manage.py makemigrations`. Com isso nós criamos uma lista de coisas que queremos migrar para o banco só que ainda não enviamos de fato
- [X] Realizando a migration
    - Sempre que executamos nosso servidor a mensagem `You have 18 unapplied migration(s).` é exibida, essa mensagem se refere à migrações pendentes que temos. Essas migrações são do ambiente administrativo do django, quando efetivarmos a migração para o banco de dados, além do nosso modelo de receitas, também seram feitas essas migrações pendentes. No terminal digite o comando `python manage.py migrate` 
    - Vá no `PHPMyAdmin` e veja as tabelas criadas a partir das migrações.
- [X] Registrando um modelo no admin
    - abra o arquivo `admin.py` para fazermos o registro de nosso modelo receitas. A paritr disso será criado um módulo de receitas no admin do django. No `admin.py` escreva o código:
        ```python
        from django.contrib import admin
        from .models import Receitas

        admin.site.register(Receitas)
        ```
    - acesse http://127.0.0.1:8000/admin
- [X] Criando um usuário para o ambiente administrativo
    - Precisamos criar um usuário para acessar a área administrativa. No terminal digite o comando `python manage.py createsuperuser` e preencha os campos.
    - Volte na área administrativa e informe o usuário e senha criados para acesar a área administrativa
    - Veja que o módulo de receitas está visível, isso só acontece porque registramos o o modelo no `admin.py`.
    - Adicione algumas receitas.
- [] Listando os dados do banco de dados
- [] 

## 📫 Contribuindo para <nome_do_projeto>
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com <nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#nome-do-projeto)<br>