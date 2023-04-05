from django.urls import path
from job.presentation.views import CreateJobView


app_name = 'job'

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create_job')
]
