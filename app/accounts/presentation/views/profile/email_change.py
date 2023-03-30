from django.views.generic import FormView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django_htmx.http import HttpResponseClientRedirect
from accounts.forms import EmailChangeForm


class ChangeEmailView(LoginRequiredMixin, FormView):

    template_name = 'accounts/profile/change_email.html'
    partial_template_name = 'accounts/profile/partials/change_email.html'
    form_class = EmailChangeForm
    success_url = reverse_lazy("accounts:login")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(ChangeEmailView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        success_message = _("Registration successful!")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        logout(self.request)
        if self.request.htmx:
            return HttpResponseClientRedirect(self.success_url)
        return super().form_valid(form)

    def get_template_names(self):
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name

    def form_invalid(self, form):
        print(form.errors.as_data())
        return super().form_invalid(form)


