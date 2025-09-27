from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto, Protuto_Tag, Categoria

def teste(request):
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
    return render(request, 'estoque/index_static.html', context)


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
    return render(request, 'estoque/index_estoque.html', context)

##
# Produtos
##
class ProdutoListView(ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'  # Nome da variável a ser usada no template
    ordering = ['nome']  # Opcional: ordena os produtos por nome
    paginate_by = 10 # Opcional: Adiciona paginação


class ProdutoTabelaListView(ListView):
    model = Produto
    template_name = 'estoque/produto_tabela_list.html'
    context_object_name = 'produtos'  # Nome da variável a ser usada no template
    ordering = ['nome']  # Opcional: ordena os produtos por nome
    paginate_by = 10 # Opcional: Adiciona paginação


# READ (Detail)
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'
    context_object_name = 'produto'

# CREATE
class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    # Lista dos campos que o usuário poderá preencher
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    # URL para onde o usuário será redirecionado após o sucesso
    success_url = reverse_lazy('estoque:produto_list')

    # Adiciona um título dinâmico ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Novo Produto'
        return context

# UPDATE
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Produto'
        return context

# DELETE
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('estoque:produto_list')
    context_object_name = 'produto'






#----------------------------------



# CATEGORIA
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria_list.html'
    context_object_name = 'categorias'
    ordering = ['identificacao']


#(Detail)

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria'
    #template_name = 'estoque/produto_detail.html'
    context_object_name = 'categoria'

#CREATE
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/produto_form.html'
    # Lista dos campos que o usuário poderá preencher
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    # URL para onde o usuário será redirecionado após o sucesso
    success_url = reverse_lazy('estoque:produto_list')

# UPDATE
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Categoria'
        return context

# DELETE
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('estoque:produto_list')
    context_object_name = 'Categoria'







