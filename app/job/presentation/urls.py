from django.urls import path
from job.presentation.views import (
    CreateJobView, JobListingsView, UpdateJobView)


app_name = 'job'

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create_job'),
    path('jobs/view/', JobListingsView.as_view(), name='view_jobs'),
    path('job/<int:pk>edit/', UpdateJobView.as_view(), name='edit_job'),
]
