from django.shortcuts import render, get_object_or_404
from galeria.models import Exercicios

def index(request):
    imagens = Exercicios.objects.filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : imagens})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Exercicios, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})

def buscar(request):
    fotografias = Exercicios.objects.filter(publicada = True)

    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if nome_buscado:
            fotografias_buscadas = fotografias.filter(nome__icontains=nome_buscado)
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias_buscadas})


def categorias(request, categoria):
    fotografias = Exercicios.objects.filter(categoria=categoria, publicada=True)
    
    return render(request, 'galeria/categorias.html', {'cards': fotografias})

