from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    context = {'page': 'Job Search | JobPortal'}
    return render(request, "index.html", context)

def sign_in(request):
    context = {'page': 'Sign In  | JobPortal Accounts'}
    return render(request, "signin.html", context)

def check_email_view(request):
    if request.method == "POST":
        data = request.POST

        email = data.get('email')
        password = data.get('password')

        user_exists = User.objects.filter(email=email).exists()
        if user_exists is not None:
            return redirect("login")

        else:
            messages.info(request, "User already exists")
            return redirect("signin")

    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")