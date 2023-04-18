from django.urls import path
from shortlist.presentation.views import (
    OpeningsView, ClearFiltersView, OpeningView,
    IndustryOpeningsView, ApplicationView, EmployeeApplicationsView)

app_name = 'shortlist'

urlpatterns = [
    path('openings/', OpeningsView.as_view(), name='openings'),
    path(
        'clear/filter/<str:filter_param>/<path:next>/',
        ClearFiltersView.as_view(), name='clear_filters'),
    path('view/opening/<slug:slug>/', OpeningView.as_view(), name='opening'),
    path('view/industry/<slug:slug>/',
         IndustryOpeningsView.as_view(), name='industry_openings'),
    path('apply/<path:next>/', ApplicationView.as_view(), name='apply'),
    path('my/applications/',
         EmployeeApplicationsView.as_view(), name='employee_applications'),
]
