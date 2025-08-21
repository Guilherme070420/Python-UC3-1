# projeto_loja/site_loja/urls.py

from django.urls import path
from . import views # Importa as views que acabamos de criar

# Define o namespace para esta aplicação
app_name = 'site_loja' 

urlpatterns = [
    path('', views.home, name='home'), 
    #path('produtos/', views.lista_produtos, name='lista_produtos'), 
    path('produtos/', views.produtos_lista, name='produtos_lista'),
    path('perfil/', views.perfil, name='perfil'), # URL para a página de perfil
]