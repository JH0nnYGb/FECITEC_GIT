from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    celular = forms.CharField(
        max_length=15,
        error_messages={'max_length': 'O número deve ter no máximo 15 caracteres.'}
    )
    endereco = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=100)
    bairro = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=2)
    formacao = forms.CharField(max_length=255)
    instituicao = forms.CharField(max_length=255, required=True) 
    municipio = forms.CharField(max_length=100, required=True)  
    estado_instituicao = forms.CharField(max_length=2, required=True)  
    formacao = forms.ChoiceField(
        choices=[
            ('Fundamental - Incompleto', 'Fundamental - Incompleto'),
            ('Fundamental - Completo', 'Fundamental - Completo'),
            ('Médio - Incompleto', 'Médio - Incompleto'),
            ('Médio - Completo', 'Médio - Completo'),
            ('Superior - Incompleto', 'Superior - Incompleto'),
            ('Superior - Completo', 'Superior - Completo'),
            ('Pós-graduação (Lato sensu) - Incompleto', 'Pós-graduação (Lato sensu) - Incompleto'),
            ('Pós-graduação (Lato sensu) - Completo', 'Pós-graduação (Lato sensu) - Completo'),
            ('Pós-graduação (Stricto sensu, nível mestrado) - Incompleto', 'Pós-graduação (Stricto sensu, nível mestrado) - Incompleto'),
            ('Pós-graduação (Stricto sensu, nível mestrado) - Completo', 'Pós-graduação (Stricto sensu, nível mestrado) - Completo'),
            ('Pós-graduação (Stricto sensu, nível doutor) - Incompleto', 'Pós-graduação (Stricto sensu, nível doutor) - Incompleto'),
            ('Pós-graduação (Stricto sensu, nível doutor) - Completo', 'Pós-graduação (Stricto sensu, nível doutor) - Completo'),
        ],
        required=True,
        
    )

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        
        # Validação personalizada para senha
        if len(password2) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        
        if password2.isdigit():
            raise ValidationError("A senha não pode ser totalmente numérica.")
        
        return password2
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'nome_completo', 'celular', 'endereco', 'cidade', 'bairro', 'estado', 
                  'formacao', 'instituicao', 'municipio', 'estado_instituicao']