from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, reverse 
from django.contrib import messages

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard_admin.html')