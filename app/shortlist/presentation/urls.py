from django.urls import path
from shortlist.presentation.views import (
    OpeningsView, ClearFiltersView, OpeningView)

app_name = 'shortlist'

urlpatterns = [
    path('openings/', OpeningsView.as_view(), name='openings'),
    path(
        'clear/filter/<str:filter_param>/',
        ClearFiltersView.as_view(), name='clear_filters'),
    path('view/opening/<slug:slug>/', OpeningView.as_view(), name='opening'),
]
