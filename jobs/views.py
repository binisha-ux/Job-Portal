from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# Create your views here.
def employer_signup(request):
    if request.method == "POST":
        data = request.POST

        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=email).exists():
            messages.info(request, "Email already existed")
            return redirect("employer_signup")

        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user , backend='django.contrib.auth.backends.ModelBackend')
        return redirect('jobportal')

    return render(request, "employer_signup.html")

def employer_home(request):
    return render(request, "employer.html")
