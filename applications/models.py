from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Application(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        REVIEWED = "REVIEWED", "Reviewed"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"

    job = models.ForeignKey("jobs.Job", on_delete=models.CASCADE, related_name="applications")
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    portfolio_url = models.URLField(blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)


    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('job', 'candidate'))

    def __str__(self):
        return f"{self.full_name} - {self.candidate.username} - {self.job.title}"