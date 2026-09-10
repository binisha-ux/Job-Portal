from django.contrib import admin
from .models import Application

# Register your models here.
@admin.register(models.admin)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "candidate", "status", "applied_at")
    list_filter = ("status", "applied_at")
    search_fields = ("job__title", "candidate__user__username", "candidate__user__email")

    ordering = ("-applied_at",)
