from django.contrib import admin
from job.models import Industry, JobListing


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    exclude = ['slug']


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    exclude = ['slug']
