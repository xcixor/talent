from django.urls import path
from django.contrib import admin
from infinite_admin.presentation.views import (
    AdvancedAdminDashboardView)


class CustomAdmin(admin.AdminSite):

    def get_urls(self):
        urls = super(CustomAdmin, self).get_urls()
        custom_urls = [
            path('',
                 admin.site.admin_view(AdvancedAdminDashboardView.as_view()),
                 name='advanced_index'),
        ] + urls
        return custom_urls


custom_admin_site = CustomAdmin(name='admin_advanced')
