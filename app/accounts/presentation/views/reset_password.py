from django.views.generic import TemplateView


class reset_passwordView(TemplateView):

    template_name = 'accounts/reset_password.html'
