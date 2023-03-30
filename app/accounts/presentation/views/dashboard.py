from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/dashboard.html'
    superuser_dashboard = 'infinite_admin/dashboard.html'

    def get_template_names(self):
        if self.request.user.is_superuser:
            return self.superuser_dashboard
        return self.template_name
