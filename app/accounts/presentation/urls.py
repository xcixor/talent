from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LogoutView, PasswordChangeView)
from accounts.presentation.views import (
    RegistrationView, LoginView, reset_passwordView,
    DashboardView, ChangeEmailView)


app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset_password/', reset_passwordView.as_view(), name='reset_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='accounts/profile/change_password.html',
        success_url=reverse_lazy('accounts:login')),
        name='change_password'),
]
