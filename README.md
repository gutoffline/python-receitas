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