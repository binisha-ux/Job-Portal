from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from .models import Application

# Create your views here.
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == "POST":
        data = request.POST

        
    


