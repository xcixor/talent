"""urls
"""
from django.urls import path
from about.presentation.views import AboutIndexView


app_name = 'about'


urlpatterns = [
    path('', AboutIndexView.as_view(), name='index')
]
