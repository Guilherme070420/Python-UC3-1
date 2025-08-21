from django.shortcuts import render # Importamos a função render

def index(request):
    """
    Esta função é a nossa view 'index'.
    Ela será responsável por exibir a página inicial da aplicação produtos.
    """
    
    # Criamos um dicionário com dados que queremos enviar para o template.
    # Por enquanto, vamos enviar um título simples.
    context = {
        'titulo': 'Bem-vindo à Página de Produtos!'
    }

    # A função render 'junta' o template com os dados e retorna uma resposta HTTP.
    return render(request, 'produtos/index_static.html', context)
