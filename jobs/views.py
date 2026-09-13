from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# Create your views here.


def create_job(request):
    if request.method == "POST":
        data = request.POST

        title = data.get('title')
        location = data.get('location')
        salary = data.get('salary')
        job_type = data.get('job_type')
        description = data.get('description')

        

        
    return render(request, "create_job.html")