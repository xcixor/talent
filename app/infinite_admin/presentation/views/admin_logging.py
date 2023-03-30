from django.views.generic import TemplateView


class LoggingView(TemplateView):

    template_name = 'infinite_admin/logging.html'
