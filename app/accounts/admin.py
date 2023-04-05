from django.contrib import admin
from accounts.models import User, CompanyDetails
from job.models import JobListing
from infinite_admin.admin import custom_admin_site


class CompanyDetailsInline(admin.StackedInline):

    model = CompanyDetails
    extra = 0


class JobListingInline(admin.StackedInline):

    model = JobListing
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CompanyDetailsInline, JobListingInline]


@admin.register(User, site=custom_admin_site)
class CustomUserAdmin(admin.ModelAdmin):
    pass
