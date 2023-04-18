from django.conf import settings
from django.contrib.auth import login
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import TemplateView, FormView
from django_htmx.http import HttpResponseClientRedirect
from django.urls import reverse_lazy
from accounts.forms import StaffRegistrationForm


class GetStaffRegistrationView(TemplateView):

    template_name = 'accounts/registration/staff/staff_registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StaffRegistrationForm(self.request)
        return context


class PostStaffRegistrationView(FormView):

    form_class = StaffRegistrationForm
    template_name = 'accounts/registration/staff/staff_registration.html'
    partial_template_name = 'accounts/registration/staff/partials/staff_registration.html'

    def form_valid(self, form):
        self.request.session.pop('registration_details', None)
        new_user = form.save()
        if not settings.DEBUG:
            form.send_account_creation_notification(new_user, self.request)
        login(self.request, new_user)
        success_message = _("Registration successful!")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return HttpResponseClientRedirect(reverse_lazy('accounts:dashboard'))

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(PostStaffRegistrationView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_invalid(self, form):
        registration_details = {}
        for key, value in self.request.POST.items():
            registration_details[key] = value
        registration_details.pop('password1', None)
        registration_details.pop('password2', None)
        self.request.session['registration_details'] = registration_details
        return super().form_invalid(form)

    def get_template_names(self):
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name


class StaffRegistrationView(View):

    def get(self, request, *args, **kwargs):
        view = GetStaffRegistrationView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostStaffRegistrationView.as_view()
        return view(request, *args, **kwargs)
