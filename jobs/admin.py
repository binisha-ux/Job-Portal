from django.contrib import admin
from django.models import Job
# Register your models here.
@admin.site.register
class JobAdmin(admin.ModelAdmin):
    list_display = ('employer', 'title', 'job_type', salary)
    list_filter = ('job_type', 'description', 'created_at')
    search_fields = ('title', description 'location', 'job_type', 'salary')
