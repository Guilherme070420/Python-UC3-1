from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto, Protuto_Tag, Categoria
from django.contrib import messages

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

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset

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
    
# CATEGORIA

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria_list.html'
    context_object_name = 'categorias'

# Ver detalhes de uma categoria
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria_detail.html'
    context_object_name = 'categoria'

# Criar nova categoria
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['identificacao', 'descricao']
    template_name = 'estoque/categoria_form.html'
    success_url = reverse_lazy('estoque:categoria_list')

# Atualizar categoria existente
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['identificacao', 'descricao']
    template_name = 'estoque/categoria_form.html'
    success_url = reverse_lazy('estoque:categoria_list')

# Excluir categoria
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/categoria_confirm_delete.html'
    success_url = reverse_lazy('estoque:categoria_list')
    
# TAG

# LIST
class ProtutoTagListView(ListView):
    model = Protuto_Tag
    template_name = 'estoque/produto_tag.html'
    context_object_name = 'tags'

# DETAIL
class ProtutoTagDetailView(DetailView):
    model = Protuto_Tag
    template_name = 'estoque/produto_tag.html'
    context_object_name = 'tag'

# CREATE
class ProtutoTagCreateView(CreateView):
    model = Protuto_Tag
    fields = '__all__'
    template_name = 'estoque/tag_form.html'
    success_url = reverse_lazy('estoque:tag_list')
    
# UPDATE
class ProtutoTagUpdateView(UpdateView):
    model = Protuto_Tag
    fields = '__all__'
    template_name = 'estoque/produto_tag.html'
    success_url = reverse_lazy('tag_list')

# DELETE
class ProtutoTagDeleteView(DeleteView):
    model = Protuto_Tag
    template_name = 'estoque/produto_tag.html'
    success_url = reverse_lazy('tag_list')


# 🛒 Adicionar ao carrinho
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho = request.session.get('carrinho', {})

    # Se já existe no carrinho, soma a quantidade
    if str(produto_id) in carrinho:
        carrinho[str(produto_id)]['quantidade'] += 1
    else:
        carrinho[str(produto_id)] = {
            'nome': produto.nome,
            'preco': float(produto.preco),
            'quantidade': 1,
            'imagem': produto.imagem.url if produto.imagem else '',
        }

    request.session['carrinho'] = carrinho
    messages.success(request, f"✅ {produto.nome} foi adicionado ao carrinho!")
    return redirect('estoque:produto_list')


# 🛒 Ver carrinho
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    total = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    return render(request, 'estoque/carrinho.html', {'carrinho': carrinho, 'total': total})


# 🛒 Remover item do carrinho
def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(produto_id)

    if produto_id_str in carrinho:
        del carrinho[produto_id_str]
        request.session['carrinho'] = carrinho
        messages.warning(request, "Item removido do carrinho.")

    return redirect('estoque:ver_carrinho')


# 🛒 Limpar carrinho
def limpar_carrinho(request):
    request.session['carrinho'] = {}
    messages.info(request, "Carrinho esvaziado.")
    return redirect('estoque:ver_carrinho')