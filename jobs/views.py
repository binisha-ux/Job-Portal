from django.shortcuts import render

# Create your views here.
def employer_signup(request):
    return render(request, "employer_signup.html")

def employer_home(request):
    return render(request, "employer.html")