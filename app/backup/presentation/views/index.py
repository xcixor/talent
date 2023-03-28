from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BackupView(LoginRequiredMixin, TemplateView):

    template_name = 'backup/backup.html'
