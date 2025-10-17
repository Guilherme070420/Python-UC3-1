# imports
from django.urls import path 

# Importamos as views da nossa aplicação (o arquivo views.py)
from . import views          

# Define o "namespace" para a aplicação
app_name = 'estoque'
 

urlpatterns = [
    # O caminho vazio '' significa a raiz da nossa aplicação 'produtos'
    path('', views.index, name='index'),
    path('teste/', views.teste, name='este'),

    ##
    # Produtos
    ##
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/listar/', views.ProdutoTabelaListView.as_view(), name='produto_tabela_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),

#CATEGORIA
     path('categorias/novo/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/listar/', views.CategoriaListView.as_view(), name='categoria_tabela_list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/deletar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    
#TAGS#

    path('tags/', views.ProtutoTagListView.as_view(), name='tag_list'),
    path('tags/<int:pk>/', views.ProtutoTagDetailView.as_view(), name='tag_detail'),
    path('tags/novo/', views.ProtutoTagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/editar/', views.ProtutoTagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/deletar/', views.ProtutoTagDeleteView.as_view(), name='tag_delete'),

   
    
    # 🛒 Carrinho
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/limpar/', views.limpar_carrinho, name='limpar_carrinho'),


    
]