from django.urls import path
from django.contrib import admin
from infinite_admin.presentation.views import (
    AdvancedAdminDashboardView, LoggingView, CloudBackupView,
    StaffView, PermissionsView, MakeShortlisterReviewerView,
    UnassignedApplicationsView)


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
            path('users/staff/',
                 admin.site.admin_view(StaffView.as_view()),
                 name='staff'),
            path('applications/unassigned/',
                 admin.site.admin_view(UnassignedApplicationsView.as_view()),
                 name='unassigned_applications'),
            path('users/<int:pk>/permissions/',
                 admin.site.admin_view(PermissionsView.as_view()),
                 name='permissions'),
            path('users/<int:pk>/permissions/shortlisting/',
                 admin.site.admin_view(MakeShortlisterReviewerView.as_view()),
                 name='shortlist_permissions'),
        ] + urls
        return custom_urls


custom_admin_site = CustomAdmin(name='basic_admin')
