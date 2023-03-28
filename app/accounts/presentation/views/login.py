from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from accounts.forms import LoginForm


class LoginView(LoginView):

    template_name = "accounts/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
            self.request.session.modified = True
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors.as_data())
        return super().form_invalid(form)

    def get_success_url(self):
        success_message = _('Welcome back ') + str(self.request.user)
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        next_url = self.request.GET.get("next", None)
        if next_url:
            return next_url
        return settings.LOGIN_REDIRECT_URL
