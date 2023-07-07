from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Exercicios
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:  ## Verifica se o usuario está logado
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    else:
        imagens = Exercicios.objects.filter(publicada=True)
        return render(request, 'galeria/index.html', {"cards" : imagens})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Exercicios, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})

def buscar(request):
    if not request.user.is_authenticated:  ## Verifica se o usuario está logado
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    fotografias = Exercicios.objects.filter(publicada = True)

    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if nome_buscado:
            fotografias_buscadas = fotografias.filter(nome__icontains=nome_buscado)
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias_buscadas})


def categorias(request, categoria):
    fotografias = Exercicios.objects.filter(categoria=categoria, publicada=True)
    
    return render(request, 'galeria/categorias.html', {'cards': fotografias})

