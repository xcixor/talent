from django.contrib import admin
from accounts.models import User, CompanyDetails


class CompanyDetailsInline(admin.TabularInline):

    model = CompanyDetails
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CompanyDetailsInline]


# admin.site.register(User, UserAdmin)
