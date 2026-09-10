from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
    headline = models.CharField(max_length=100)
    bio = models.TextField()
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    skills = models.CharField(max_length=255, help_text="Comma-separated-skills", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Candidate Profile"

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True)
    company_description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

