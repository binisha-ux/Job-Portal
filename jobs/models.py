from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    class JobType(models.TextChoices):
        FULL_TIME = 'FULL_TIME', "Full Time"
        PART_TIME = 'PART_TIME', "Part Time"
        REMOTE = 'REMOTE', "Remote"

    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JobType.choices, default=JobType.FULL_TIME)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
