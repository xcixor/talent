from django.conf import settings
from django.contrib.auth import login
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import TemplateView, FormView
from accounts.forms import RegistrationForm


class GetRegistrationView(TemplateView):

    template_name = 'accounts/registration/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegistrationForm(self.request)
        return context


class PostRegistrationView(FormView):

    form_class = RegistrationForm
    template_name = 'accounts/registration/registration.html'
    success_url = '/accounts/dashboard/'

    def form_valid(self, form):
        self.request.session.pop('registration_details', None)
        new_user = form.save()
        if not settings.DEBUG:
            form.send_account_activation_email(new_user, self.request)
        login(self.request, new_user)
        success_message = _("Registration successful!")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(PostRegistrationView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_invalid(self, form):
        print(form.errors.as_data())
        registration_details = {}
        for key, value in self.request.POST.items():
            registration_details[key] = value
        registration_details.pop('password1', None)
        registration_details.pop('password2', None)
        self.request.session['registration_details'] = registration_details
        return super().form_invalid(form)


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        view = GetRegistrationView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostRegistrationView.as_view()
        return view(request, *args, **kwargs)
