from django.views.generic import TemplateView


class ResetPasswordView(TemplateView):

    template_name = 'accounts/reset_password.html'
