from django.urls import path
from django.contrib.auth.views import (
    LogoutView)
from accounts.presentation.views import RegistrationView
from accounts.presentation.views import LoginView
from accounts.presentation.views import reset_passwordView
from accounts.presentation.views import DashboardView

app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset_password/', reset_passwordView.as_view(), name='reset_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
