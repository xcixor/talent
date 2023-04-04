from django.contrib import admin
from accounts.models import User, CompanyDetails
from infinite_admin.admin import custom_admin_site


class CompanyDetailsInline(admin.TabularInline):

    model = CompanyDetails
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CompanyDetailsInline]


@admin.register(User, site=custom_admin_site)
class CustomUserAdmin(admin.ModelAdmin):
    pass
