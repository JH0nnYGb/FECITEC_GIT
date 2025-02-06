from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse 
from django.contrib import messages
from django.core.paginator import Paginator

from core.models import Participante
from core.models import SubmissionToWork
from django.db.models import Count

from core.forms import ComissionMembrerCreationForm

# IMPORTACAO DO MODELOS CORE
from core.models import Commission
from core.models import User,GrupoPersonalizado, Participante,Instituicao

# FIM IMPORTACAO DO MODELOS CORE

@login_required
def views_admin_dashboard(request):
    return render(request, 'dashboard_admin.html')

@login_required
def views_admin_submission(request):
    submissions = SubmissionToWork.objects.all()
    return render(request, 'admin_screen_submission.html',{'submissions':submissions})

@login_required
def views_admin_jurors(request):
    return render(request, 'admin_screen_jurors.html' )

@login_required
def views_admin_evaluators(request):
    return render (request, 'admin_screen_evaluators.html')

@login_required
def views_admin_reviews(request):
    return render (request, 'admin_screen_reviews.html')

@login_required
def views_admin_participants(request):
    participantes = Participante.objects.annotate(
        total_submissoes=Count('submissions')
    )

    context = {
        'participantes': participantes,
    }

    return render(request, 'admin_screen_participants.html', context)

@login_required
def views_add_members(request):
    form = ComissionMembrerCreationForm()

    if request.method == 'POST':
        form = ComissionMembrerCreationForm(request.POST, request.FILES)
        if form.is_valid():
            name_member = form.cleaned_data['name_member']
            email_member = form.cleaned_data['email_member']
            phone_member = form.cleaned_data['phone_member']
            formation_member = form.cleaned_data['formation_member']
            member_profile = form.cleaned_data['member_profile']
            position_member = form.cleaned_data['position_member']

            if Commission.objects.filter(email_member=email_member).exists():
                messages.error(request,"Este e-mail já está cadastrado.")
                

            if Commission.objects.filter(phone_member=phone_member).exists():
                messages.error(request, "Este telefone já está cadastrado.")
                

            user = User.objects.create(username=name_member,email=email_member)
            user.first_name=name_member
            user.save()
            
            
            #criar o Membro da comissao no banco de dados 
            commission = Commission.objects.create(
                user=user,
                name_member= form.cleaned_data['name_member'],
                email_member= form.cleaned_data['email_member'],
                phone_member= form.cleaned_data['phone_member'],
                formation_member= form.cleaned_data['formation_member'],
                member_profile= form.cleaned_data['member_profile'],
                position_member= position_member
            )

            grupo_nomes = {
                'Jurado': 'Jurado',
                'Avaliador': 'Avaliador',
                'Administrador': 'Administrador',
            }

            for funcao in position_member:
                if funcao in grupo_nomes:
                    grupo = GrupoPersonalizado.objects.get(nome=grupo_nomes[funcao])
                    grupo.usuarios.add(user)


                

            messages.success(request,"Membro adicionado com sucesso!")
            return redirect('admin_fecitec:admin_commission')
        
    return render(request, 'admin_registered_member_comission.html', {'form':form})


@login_required
def views_admin_commission(request):
    members = Commission.objects.all()
    comission_paginator = Paginator(members, 1)
    members_num = request.GET.get('page')
    members_page = comission_paginator.get_page(members_num)

    context = {
        'comission': members_page,
        'current_page': members_page.number
    }


    return render (request, 'admin_screen_commission.html', context)

@login_required
def viewa_admin_contacts(request):
    return render(request, 'admin_screen_contacts.html')


