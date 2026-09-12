from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    context = {'page': 'Job Search | JobPortal'}
    return render(request, "index.html", context)

def sign_up(request):
    if request.method == "POST":
        data = request.POST

        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=email).exists():
            messages.info(request, "Email already existed. ")
            return redirect("signup")

        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "user created successfully. ")
        return redirect("jobportal")

    return render(request, "signup.html")





def sign_in(request):
    if request.method == "POST":
        data = request.POST

        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("feeds")

        else:
            messages.info(request, "Invalid email or password")
            return redirect("signin")

    context = {'page': 'Sign In  | JobPortal Accounts'}
    return render(request, "signin.html", context)



def login_view(request):
    return render(request, "login.html")