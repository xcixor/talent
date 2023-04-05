from django.views.generic import ListView
from job.models import JobListing


class JobListingsView(ListView):

    model = JobListing
    template_name = 'job/jobs.html'
    context_object_name = 'jobs'
