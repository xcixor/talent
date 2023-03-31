from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from accounts.forms import UpdateModeOfContactForm
from accounts.models import User


class UpdateModeOfContactView(UpdateView):

    model = User
    form_class = UpdateModeOfContactForm
    template_name = 'accounts/profile/change_mode_of_contact.html'
    success_url = reverse_lazy("accounts:dashboard")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(UpdateModeOfContactView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        success_message = _("Update successful.")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        success_message = _("Something went wrong.")
        messages.add_message(
            self.request, messages.ERROR, success_message)
        return super().form_invalid(form)
