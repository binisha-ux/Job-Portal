from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Job

# Create your views here.

@login_required
def create_job(request):
    if request.method == "POST":
        data = request.POST

        job_title = data.get('job_title')
        location = data.get('location')
        salary = data.get('salary')
        job_type = data.get('job_type')
        description = data.get('description')
        company_name = data.get('company_name')

        Job.objects.create(
            employer=request.user, 
            title=job_title,
            location=location, 
            salary=salary,
            job_type=job_type, 
            description=description,
            company_name=company_name
        )

        messages.success(request, "Job created successfully.")
        return redirect('create_job')
    
    jobs = Job.objects.filter(employer=request.user).order_by('-id')

    context = {'jobs': jobs}
        
    return render(request, "create_job.html", context)


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("create_job")

    return redirect("create_job")

# Job views and handlers
@login_required
def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == "POST":
        data = request.POST

        job.title = data.get('job_title', job.title)
        job.location = data.get('location', job.location)
        job.salary = data.get('salary', job.salary)
        job.job_type = data.get('job_type', job.job_type)
        job.description = data.get('description', job.description)
        job.company_name = data.get('company_name', job.company_name)

        job.save()

        messages.success(request, "Job created successfully.")
        return redirect('create_job')


    return render(request, "update_job.html", {'job':job})

