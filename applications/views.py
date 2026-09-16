from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from .models import Application
from django.contrib import messages 

# Create your views here.
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == "POST":
        data = request.POST

        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')
        portfolio_url = data.get('portfolio_url')
        cover_letter = data.get('cover_letter')
        resume = request.FILES.get('resume')

        if Application.objects.filter(job=job, candidate=request.user).exists():
            messages.warning(request, "You have already applied for this job.")
            return redirect("search_jobs")


        Application.objects.create(
            job = job,
            candidate = request.user,
            full_name = full_name, 
            email = email, 
            phone = phone, 
            portfolio_url = portfolio_url, 
            cover_letter = cover_letter,
            resume = resume
        )
        return redirect("search_jobs")

    return render(request, "my_applications.html", {'job':job})




 

    


