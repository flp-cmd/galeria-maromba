from django import forms
import re
from django.contrib.auth.models import User

class loginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite seu nome"
            }
        )
    )
    
    senha_login = forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : 'Digite sua senha'
            }
        )
    )
    
class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Digite seu nome completo'
            }
        )
    )
    
    email_cadastro = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Digite seu email'
            }
        )
    )
    
    senha_1 = forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : 'Digite sua senha'
            }
        )
    )
    
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : 'Digite sua senha novamente'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            padrao = r'\d'
            if re.search(padrao, nome):
                raise forms.ValidationError('Números não são permitidos no campo nome')
            return nome
        
    def clean_senha_2(self):
        senha1 = self.cleaned_data.get('senha_1')
        senha2 = self.cleaned_data.get('senha_2')
        
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("Senhas não coincidem")
            return senha2
        
    def clean_email_cadastro(self):
        email = self.cleaned_data.get('email_cadastro')
        
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email já cadastrado')
            return email