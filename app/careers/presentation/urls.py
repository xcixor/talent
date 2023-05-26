from django.urls import path
from careers.presentation.views import IndexView, CareerView


app_name = 'careers'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', CareerView.as_view(), name='career'),
]
