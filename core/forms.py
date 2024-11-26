from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    celular = forms.CharField(max_length=15)
    endereco = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=100)
    bairro = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=2)
    formacao = forms.CharField(max_length=255)
    instituicao = forms.CharField(max_length=255, required=True) 
    municipio = forms.CharField(max_length=100, required=True)  
    estado_instituicao = forms.CharField(max_length=2, required=True)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'nome_completo', 'celular', 'endereco', 'cidade', 'bairro', 'estado', 
                  'formacao', 'instituicao', 'municipio', 'estado_instituicao']