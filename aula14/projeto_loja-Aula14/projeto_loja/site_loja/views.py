# core/site/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Importa o decorador
from .forms import UserUpdateForm, PerfilUpdateForm
from .models import Perfil # Importa o modelo Perfil
from django.contrib import messages # Importa mensagens para feedback ao usuário

def home(request):
    """
    View para a página inicial do site.
    """
    return render(request, 'site_loja/home.html')

##
# Versão Original
##
def lista_produtos_v1(request):
    """
    View para listar os produtos.
    """
    context = {
        'produtos': '',
        'titulo': 'Bem-vindo à Página de Produtos!'
    }
    return render(request, 'site_loja/lista_produtos.html', context)

##
# Versão - Aula 09
##
def produtos_lista(request):
    # Lógica para obter a lista de produtos
    produtos = [
        {'nome': 'Smartphone X', 'preco': 1500},
        {'nome': 'Notebook Y', 'preco': 3000},
        {'nome': 'Fone de Ouvido Z', 'preco': 200},
    ]
    titulo: 'Bem-vindo à Página de Produtos!'
    return render(request, 'site_loja/produtos_lista.html', {'produtos': produtos})


##
# Versão - Aula 10
##
@login_required # Garante que o usuário esteja logado para acessar esta view
def perfil(request):
    if request.method == 'POST':
        # Popula os formulários com os dados enviados pelo POST e instâncias existentes
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Seu perfil foi atualizado com sucesso!')
            return redirect('site_loja:perfil') # Redireciona para evitar reenvio do formulário
        else:
            messages.error(request, 'Ocorreu um erro ao atualizar seu perfil. Verifique os dados.')

    else: # Se a requisição for GET (primeira vez que a página é acessada)
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'site_loja/perfil.html', context)