from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'page': 'Job Search | JobPortal'}
    return render(request, "index.html", context)

def sign_in(request):
    context = {'page': 'Sign In  | JobPortal Accounts'}
    return render(request, "signin.html", context)