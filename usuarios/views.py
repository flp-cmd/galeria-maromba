from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from usuarios.forms import loginForms, cadastroForms
from django.contrib import messages

def login(request):

    if request.method == 'POST':
        form = loginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha_login'].value()
            
            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Olá {nome}, seja bem vindo!')
                return redirect('index')
            
            else:
                messages.error(request, 'Erro ao efetuar login, tente novamente!')
                return redirect('login')
    else:
        form = loginForms()
        
    return render(request, 'usuarios/login.html', {'form' : form})

def cadastro(request):
    
    if request.method == 'POST':
        form = cadastroForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email_cadastro'].value()
            senha_1 = form['senha_1'].value()

            usuario = User.objects.create_user(
                username=nome,
                password=senha_1,
                email=email
            )
            
            usuario.save()
            messages.success(request, f'Cadastro realizado com sucesso, seja bem vindo {nome}!')
            return redirect('login')
            
    else:
        form = cadastroForms()
    
    return render(request, 'usuarios/cadastro.html', {'form' : form})
                
def logout(request):
    nome = request.user.username
    if nome != '':
        auth.logout(request)
        messages.success(request, f'Até mais {nome}, volte sempre!')
    
    return redirect('login')
