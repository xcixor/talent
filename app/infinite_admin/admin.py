from django.urls import path
from django.contrib import admin
from infinite_admin.presentation.views import (
    AdvancedAdminDashboardView, LoggingView, CloudBackupView)


class CustomAdmin(admin.AdminSite):

    def get_urls(self):
        urls = super(CustomAdmin, self).get_urls()
        custom_urls = [
            path('',
                 admin.site.admin_view(AdvancedAdminDashboardView.as_view()),
                 name='basic_index'),
            path('logging/',
                 admin.site.admin_view(LoggingView.as_view()),
                 name='logging'),
            path('logging/backup/',
                 admin.site.admin_view(CloudBackupView.as_view()),
                 name='backup_logs'),
        ] + urls
        return custom_urls


custom_admin_site = CustomAdmin(name='basic_admin')
