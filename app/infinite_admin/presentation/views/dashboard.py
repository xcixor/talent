from django.views.generic import TemplateView


class AdvancedAdminDashboardView(TemplateView):

    template_name = 'infinite_admin/dashboard.html'
