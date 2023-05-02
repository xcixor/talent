from django.urls import path
from contact.presentation.views import ContactView


app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='index')
]
