from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse 
from django.contrib import messages

from core.models import Participante
from core.models import SubmissionToWork
from django.db.models import Count


@login_required
def views_admin_dashboard(request):
    return render(request, 'dashboard_admin.html')

@login_required
def views_admin_submission(request):
    submissions = SubmissionToWork.objects.all()
    return render(request, 'admin_screen_submission.html',{'submissions':submissions})

def views_admin_jurors(request):
    return render(request, 'admin_screen_jurors.html' )

def views_add_members(request):
    return render(request, 'admin_registered_member_comission.html')

def views_admin_evaluators(request):
    return render (request, 'admin_screen_evaluators.html')

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


def views_admin_commission(request):
    return render (request, 'admin_screen_commission.html')

def viewa_admin_contacts(request):
    return render(request, 'admin_screen_contacts.html')


