from django.views.generic.edit import CreateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from shortlist.models import Application
from django.contrib.auth.mixins import LoginRequiredMixin
from shortlist.forms import ApplicationForm


class ApplicationView(LoginRequiredMixin, CreateView):

    model = Application
    form_class = ApplicationForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        application = form.save()
        if application.id:
            success_message = _("Application successful.")
            messages.add_message(
                self.request, messages.SUCCESS, success_message)
        else:
            error_message = _("Something went wrong.")
            messages.add_message(
                self.request, messages.ERROR, error_message)
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(ApplicationView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self) -> str:
        next = self.kwargs.get('next')
        return next

    def form_invalid(self, form):
        error_message = _("Something went wrong.")
        messages.add_message(
            self.request, messages.ERROR, error_message)
        return redirect(self.kwargs.get('next'))
