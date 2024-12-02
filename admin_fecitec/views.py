from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse 
from django.contrib import messages

@login_required
def views_admin_dashboard(request):
    return render(request, 'dashboard_admin.html')


def views_admin_submission(request):
    return render(request, 'admin_screen_submission.html')

def views_admin_jurors(request):
    return render(request, 'admin_screen_jurors.html' )

def views_admin_evaluators(request):
    return render (request, 'admin_screen_evaluators.html')

def views_admin_reviews(request):
    return render (request, 'admin_screen_reviews.html')

def views_admin_participants(request):
    return render(request, 'views_admin_participants.html')

def views_admin_commission(request):
    return render (request, 'admin_screen_commission.html')

def viewa_admin_contacts(request):
    return render(request, 'admin_screen_contacts.html')