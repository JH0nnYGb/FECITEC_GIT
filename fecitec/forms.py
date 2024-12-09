from django import forms
from django.core.mail.message import EmailMessage
import re
from django.core.exceptions import ValidationError
from .models import SubmissionToWork

def validate_phone_number(value):
    phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_pattern.match(value):
        raise ValidationError('Digite um número de telefone válido.')

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    phone_number = forms.CharField(
        label='', 
        max_length=15,
        required=True,
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={
            'placeholder': 'Número',
            'id': 'telephone'
        }),
    )
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Escreva sua mensagem'}))

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        phone_number = self.cleaned_data['phone_number']

        content = f'Nome: {name}\nE-mail: {email}\nNúmero: {phone_number}\nMensagem: {message}'

        mail = EmailMessage (
            subject = 'Solicitacao de contato',
            body = content,
            from_email = 'contadeusarnoif@gmail.com',
            to = ['contadeusarnoif@gmail.com',],
            headers = {'Reply-to': email}
        )

        mail.send()

class SubmissionToWorkForm(forms.ModelForm):
    class Meta:
        model = SubmissionToWork
        fields = ['school_name', 'area', 'municipality', 'title', 'sub_area', 'summary', 'state', 'formation', 'arquivo_modelo', 'form_of_presentation', 'participante']