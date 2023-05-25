from django.urls import path
from careers.presentation.views import IndexView


app_name = 'careers'
urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
