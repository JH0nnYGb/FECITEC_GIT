from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import SubmissionToWork
from .models import Commission

class ParticipantCreationForm(UserCreationForm):
    nome_participante = forms.CharField(
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

    email_participante = forms.EmailField(
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
        label='Telefone',
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Numero de telefone'}),
        required=True,
    )

    endereco = forms.CharField(
        label='Endereço',
        max_length=255,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'Endereço'})
    )

    municipio_participante = forms.CharField(
        label='Municipio do participante',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'Seu Municipio'})
    )

    cep_pacticipante = forms.CharField(
        label='Cep da sua cidade',
        max_length=200,
        widget=forms.TextInput(attrs={'class':'fields','placeholder':'Cep da sua cidade'})
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

    

    class Meta:
        model = User
        fields = [
            'nome_participante', 'username', 'email', 'password1', 'password2',  
            'celular', 'endereco', 'municipio_participante', 'bairro', 'estado_participante', 
            'formacao_participante','cep_pacticipante',
        ]

#######FROMULARIO DE SUBMISSAO DE TRABALHOS ###########
class SubmissionToWorkForm(forms.ModelForm):
    class Meta:
        model = SubmissionToWork
        fields = ['school_name', 'area', 'municipality', 'title', 'sub_area', 'summary', 'state', 'formation', 'arquivo_modelo', 'form_of_presentation', 'participante']

############ FIM OD FORMULARI DE SUBMISSOA ############



# Formulario do cadastro dos membros da comissao 

class ComissionMembrerCreationForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['name_member','email_member','phone_member','formation_member','position_member','member_profile',]

    name_member = forms.CharField(
        label='Nome completo do membro',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Nome Completo'}),
        required=True,
    )

    email_member= forms.CharField(
        label='Email',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Email'}),
        required=True,
    )
    
    phone_member= forms.CharField(
        label='Telefone',
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'fields', 'placeholder': 'Numero de telefone'}),
        required=True,
    )

    formation_member= forms.ChoiceField(
        choices=[
            ('Mestre', 'Mestre'),
            ('Doutor', 'Doutor'),
            ('Especialista', 'Especialista'),
        ],
        widget=forms.Select(attrs={'class':'fields'}),
        label='Formação do Membro',
        required=True,
    )

    member_profile= forms.ImageField(
        label='Foto',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'fields'}),
        
    )

    position_member = forms.MultipleChoiceField(
        choices=[
            ('Jurado','Jurado'),
            ('Avaliador','Avaliador'),
            ('Administrador','Administrador'),    
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'fields', 'id':'checkbox_function'}),
        label='Funções do Membro',
        required=False,
    )

    password1 = forms.CharField(
        label='Defina uma senha',
        widget=forms.PasswordInput(attrs={'class': 'fields', 'placeholder': 'Senha'}),
        required=True,
    )

    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={'class': 'fields', 'placeholder': 'Confirmar Senha'}),
        required=True,
    )

   

     
#fim  Formulario do cadastro dos membros da comissao 
