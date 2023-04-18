from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/dashboard.html'
    superuser_dashboard = 'infinite_admin/dashboard.html'
    employer_dashboard = 'accounts/profile/employer/dashboard.html'
    staff_dashboard = 'accounts/profile/staff/dashboard.html'

    def get_template_names(self):
        if self.request.user.is_superuser:
            return self.superuser_dashboard
        if self.request.user.is_staff:
            return self.staff_dashboard
        elif self.request.user.type_of_user == 'EMPLOYER':
            return self.employer_dashboard
        return self.template_name
