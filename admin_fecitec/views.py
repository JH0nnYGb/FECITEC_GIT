from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404, reverse 
from django.contrib import messages
from django.core.paginator import Paginator

from core.models import Participante
from core.models import SubmissionToWork
from django.db.models import Count

from core.forms import ComissionMembrerCreationForm
from django.db import IntegrityError

# IMPORTACAO DO MODELOS CORE
from core.models import Commission
from core.models import User,GroupsFecitec, Participante,Instituicao

# FIM IMPORTACAO DO MODELOS CORE


from django.http import HttpResponseBadRequest

@login_required
def views_admin_dashboard(request):
    return render(request, 'dashboard_admin.html')

@login_required
def views_admin_submission(request):
    submissions = SubmissionToWork.objects.all()

    contex = {
        'submission':submissions
    }
    
    return render(request, 'admin_screen_submission.html',contex)

@login_required
def views_admin_jurors(request):
    # Pega o grupo "Jurado"
    juror_group = GroupsFecitec.objects.get(namegroup='Jurado')
    # Pega todos os usuários do grupo
    juror_users = juror_group.usuarios.all()
    # Lista de e-mails dos usuários do grupo
    juror_emails = [user.email for user in juror_users]
    # Filtra os membros da Commission pelo e-mail (garantindo que não exista erros por escrita  )
    commission_jurors = Commission.objects.filter(email_member__in=juror_emails)
    
    return render(request, 'admin_screen_jurors.html', {'commission_jurors': commission_jurors})

@login_required
def views_admin_evaluators(request):
    evaluators_group = GroupsFecitec.objects.get(namegroup='Avaliador')
    
    evaluators_group_users = evaluators_group.usuarios.all()
   
    evaluators_emails = [user.email for user in evaluators_group_users]

    commission_evaluators = Commission.objects.filter(email_member__in=evaluators_emails)

    return render (request, 'admin_screen_evaluators.html', {'commission_evaluators': commission_evaluators})

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
        
        # Inicializando variáveis para controle de erros
        errors = []

        
        if form.is_valid():
            name_member = form.cleaned_data['name_member']
            email_member = form.cleaned_data['email_member']
            phone_member = form.cleaned_data['phone_member']
            formation_member = form.cleaned_data['formation_member']
            member_profile = form.cleaned_data['member_profile']
            position_member = form.cleaned_data['position_member']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2'] 

            # Validação de senhas
            if password1 != password2:
                errors.append("As senhas não coincidem.")
            
            # Validação de campos obrigatórios
            if not name_member:
                errors.append("O nome do membro é obrigatório.")
            if not email_member:
                errors.append("O e-mail do membro é obrigatório.")
            if not phone_member:
                errors.append("O telefone do membro é obrigatório.")
            if not formation_member:
                errors.append("A formação do membro é obrigatória.")
            if not position_member:
                errors.append("A posição do membro é obrigatória.")

            if password1.isdigit():
                messages.error(request, "A senha não pode ser totalmente numérica.")
                
            
            # Verificar se o e-mail já está cadastrado
            if User.objects.filter(email=email_member).exists():
                errors.append("Este e-mail já está cadastrado.")

            # Verificar se o telefone já está cadastrado
            if Commission.objects.filter(phone_member=phone_member).exists():
                errors.append("Este telefone já está cadastrado.")

            # Se houver erros, mostrar as mensagens de erro
            if errors:
                for error in errors:
                    messages.error(request, error)
                return render(request, 'admin_registered_member_comission.html', {'form': form})

            try:
                # Criar o usuário
                user = User.objects.create(username=name_member, email=email_member)
                user.first_name = name_member
                user.set_password(password1)
                user.save()

                # Criar o membro da comissão
                commission = Commission.objects.create(
                    user=user,
                    name_member=name_member,
                    email_member=email_member,
                    phone_member=phone_member,
                    formation_member=formation_member,
                    member_profile=member_profile,
                    position_member=position_member
                )

                grupo_nomes = {
                    'Jurado': 'Jurado',
                    'Avaliador': 'Avaliador',
                    'Administrador': 'Administrador',
                }

                for funcao in position_member:
                    if funcao in grupo_nomes:
                        try:
                            grupo = GroupsFecitec.objects.get(namegroup=grupo_nomes[funcao])
                            grupo.usuarios.add(user)
                        except GroupsFecitec.DoesNotExist:
                            errors.append(f"Grupo '{funcao}' não encontrado.")
                            return render(request, 'admin_registered_member_comission.html', {'form': form})

                if not errors:
                    messages.success(request, "Membro adicionado com sucesso!")
                    return redirect('admin_fecitec:admin_add_member')

            except IntegrityError:
                messages.error(request, "Erro ao cadastrar usuário. Tente novamente.")
                return render(request, 'admin_registered_member_comission.html', {'form': form})

        else:
            # Se o formulário não for válido, exibe os erros do próprio Django
            for field, errors in form.errors.items():
                if field == "position_member":
                    messages.error(request, "A posição do membro é obrigatória.")
                else:
                    for error in errors:
                        messages.error(request,error)
                    print(errors)
            return render(request, 'admin_registered_member_comission.html', {'form': form})

    return render(request, 'admin_registered_member_comission.html', {'form': form})


@login_required
def views_edit_member(request):
    if request.method == "POST":
        print(request.POST)

        member_id= request.POST.get("memberId")
        print( member_id )
        member = get_object_or_404(Commission, id=member_id)
        
        member.name_member = request.POST.get("name")
        member.email_member = request.POST.get("email")
        member.phone_member = request.POST.get("phone")



         # Salvando Formação
        selected_formations = request.POST.getlist("formation")
        member.formation_member = ", ".join(selected_formations)

        # Salvando Funções
        selected_functions = request.POST.getlist("funcao")
        member.position_member = ", ".join(selected_functions)


        available_groups = GroupsFecitec.objects.filter(nome__in=selected_functions)
        select_groups = GroupsFecitec.objects.filter(nome__in=selected_functions)

        for group in available_groups: 
            member.user.grupos_fecitec.remove(group)

        member.user.grupos_fecitec.add(*select_groups)

        member.save()
 
        print(f"Name: {member.name_member}")
        print(f"Formation: {member.formation_member}")
        print(f"Functions: {member.position_member}")

        messages.success(request, "Alterações salvas com sucesso!")
       
        return redirect( "admin_fecitec:admin_commission")
    
    return HttpResponseBadRequest("Método inválido")

@login_required
def views_admin_commission(request):
    members = Commission.objects.all()
    comission_paginator = Paginator(members, 6)
    members_num = request.GET.get('page_membros')
    members_page = comission_paginator.get_page(members_num)

    context = {
        'comission': members_page,
        'current_page': members_page.number
    }   

    return render (request, 'admin_screen_commission.html', context)

@login_required
def viewa_admin_contacts(request):
    return render(request, 'admin_screen_contacts.html')


