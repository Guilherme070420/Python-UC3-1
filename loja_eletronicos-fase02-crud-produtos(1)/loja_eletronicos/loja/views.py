# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .forms import SignUpForm, UserForm, ProfileForm
from .models import Perfil
from django.contrib.auth.models import User

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('loja:profile')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # cria o perfil (caso não usamos signals)
            Perfil.objects.create(usuario=user)
            messages.success(request, 'Conta criada com sucesso. Faça login.')
            return redirect('loja:login')
    else:
        form = SignUpForm()
    return render(request, 'loja/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('loja:profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # respeita ?next= se houver
            next_url = request.GET.get('next') or request.POST.get('next') or reverse('loja:profile')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'loja/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da conta.')
    return redirect('estoque:index')

@login_required
def profile_view(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    return render(request, 'loja/profile.html', {'perfil': perfil})

@login_required
def profile_edit(request):
    user = request.user
    perfil, _ = Perfil.objects.get_or_create(usuario=user)
    if request.method == 'POST':
        uform = UserForm(request.POST, instance=user)
        pform = ProfileForm(request.POST, request.FILES, instance=perfil)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('loja:profile')
    else:
        uform = UserForm(instance=user)
        pform = ProfileForm(instance=perfil)
    return render(request, 'loja/profile_edit.html', {'uform': uform, 'pform': pform})
