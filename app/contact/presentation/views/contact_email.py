from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from common.email import HtmlEmailMixin
from contact.forms import ContactEmailForm


class ContactEmailView(FormView, HtmlEmailMixin):

    template_name = 'contact/index.html'
    form_class = ContactEmailForm
    success_url = reverse_lazy('contact:index')

    def form_valid(self, form):
        success_message = _("Thank you for contacting us. We will be "
                            "getting back to you shortly!")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        error_message = _("Something went wrong!")
        messages.add_message(
            self.request, messages.ERROR, error_message)
        return super().form_invalid(form)
