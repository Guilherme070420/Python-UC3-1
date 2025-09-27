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

    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='Categoria_detail'),
    #path('Categoria/listar/', views.CategoriaTabelaListView.as_view(), name='Categoria_list'),
    #path('Categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='Categoria_detail'),
    #path('Categoria/novo/', views.CategoriaCreateView.as_view(), name='Categoria_create'),
    #path('Categoria/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='Categoria_update'),
    #path('Categoria/<int:pk>/deletar/', views.CategoriaDeleteView.as_view(), name='Categoria_delete'),
   

]