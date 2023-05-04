from django.urls import path
from index.presentation.views import IndexView, ServiceView

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('service/<slug:slug>/', ServiceView.as_view(), name='service'),
]
