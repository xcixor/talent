from django.urls import path
from index.presentation.views import (
    IndexView, ServiceView, ServiceIndexView, VisaServiceDetails)

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServiceIndexView.as_view(), name='services'),
    path('visa/', VisaServiceDetails.as_view(), name='visa'),
    path('service/<slug:slug>/', ServiceView.as_view(), name='service'),
]
