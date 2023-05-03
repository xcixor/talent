from django.urls import path
from contact.presentation.views import ContactView, ContactEmailView


app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='index'),
    path('email/send/', ContactEmailView.as_view(), name='send_email'),
]
