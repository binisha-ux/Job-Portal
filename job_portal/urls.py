"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import home , sign_in,  sign_up
from accounts.views import employer_signup, employer_home, employer_signin
from jobs.views import create_job, delete_job


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="jobportal"),
    path('sign in/', sign_in, name="signin"),
    path('accounts/', include('allauth.urls')),
    path('signup/', sign_up, name="signup"),
    path('employer_signup/', employer_signup, name="employer_signup"),
    path('employer_home/', employer_home, name="employer_home"),
    path('employer_signin/', employer_signin, name="employer_signin"),
    path('createjob/', create_job, name="create_job"),
    path('deletejob/<int:job_id>/', delete_job, name="delete_job"),


    
    
]
