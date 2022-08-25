## __init__.py 
que diz ao Python que este diretório deve ser considerado um pacote.

## settings.py 
é um arquivo extremamente importante e útil para nosso trabalho, pois contém todas as configurações relacionadas a nossa aplicação, e inclusive podemos mudar o idioma da aplicação, substituindo en-us por pt-br em LANGUAGE_CODE =. Já o TIME_ZONE = será usado para São Paulo, e para descobrir o que escrever, digitamos "django timezone list" na busca do navegador para acessar este link que possui uma lista para cada localidade. Descoberta a referência, substituímos UTC por America/Sao_Paulo e salvamos o arquivo. Com isso, a hora marcada na aplicação corresponde a este fuso horário.

## urls.py 
é a declaração de todas as urls para nosso projeto, como um índice do site movido dentro de Django onde serão cadastradas.

## wsgi.py 
é um ponto de integração para servidores Web compatíveis ao WSGI. Não veremos sobre esta questão neste treinamento, pois abordaremos somente as partes mais elementares.

Se a sua aplicação web seguir a WSGI, poderá ser usada em qualquer servidor web que suporte WSGI também. Além disso existem middlewares que são como plugins, podem ser colocados em qualquer aplicação WSGI.

### WSGI é apenas para Python?
Sim, a especificação WSGI pressupõe que você deve escrever uma função em python que será chamada pelo servidor.

Hoje em dia a maioria dos frameworks python, como django, pylons, flask suportam o formato WSGI, de forma que as aplicações desenvolvidas podem ser publicadas em qualquer servidor WSGI.
https://pt.stackoverflow.com/questions/365419/o-que-seria-wsgi