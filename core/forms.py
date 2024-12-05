from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class ParticipantCreationForm(UserCreationForm):
    nome_completo = forms.CharField(
        label='Nome completo',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Nome Completo'}),
        required=True,
    )

    username = forms.CharField(
        label='Nome de usuario',
        max_length=255, 
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Nome de Usuário'}),
        required=True,
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'fields', 'placeholder': 'E-mail'}),
        required=True,
    )
    
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'fields', 'placeholder': 'Senha'}),
        required=True,
    )
    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'class': 'fields', 'placeholder': 'Confirmar Senha'}),
        required=True,
    )

    celular = forms.CharField(
        label='Número de celular',
        max_length=15, 
        widget=forms.NumberInput(attrs={'class': 'fields', 'placeholder': 'Celular'}),
        required=True,
    )

    endereco = forms.CharField(
        label='Endereço',
        max_length=255,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'Endereço'})
    )

    cidade = forms.CharField(
        label='Cidade',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'cidade'})
    )

    bairro = forms.CharField(
        label='Bairro',
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Bairro'})
    )

    estado_participante = forms.ChoiceField(
        choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), 
                 ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
                 ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
                 ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                 ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
                 ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                 ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')],
        
        widget=forms.Select(attrs={'class':'fields'}),
        label='Estado do participante',
        required=True
    )

    formacao_participante = forms.ChoiceField(
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
        widget=forms.Select(attrs={'class':'fields'}),
        label='Formação do participante',
        required=True,
        
    )

############################# DADOS DA INSTITUICAO ############################################################
    nome_instituicao = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Nome da Instituição'}),
        label='Nome da Instituição',
        required=True,
    )


    municipio = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'Municipio da Instituição'}),
        label='Municipio da Instituição',
        required=True,
    )

    estado_instituicao = forms.ChoiceField(
        choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), 
                 ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
                 ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
                 ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                 ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
                 ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                 ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')],
        widget=forms.Select(attrs={'class':'fields'}),
        label='Estado da Instituição',
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
        fields = [
            'username', 'email', 'password1', 'password2', 'nome_completo', 
            'celular', 'endereco', 'cidade', 'bairro', 'estado_participante', 
            'formacao_participante', 'nome_instituicao', 'municipio', 'estado_instituicao',
        ]