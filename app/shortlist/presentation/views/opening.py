from django.views.generic import DetailView
from job.models import JobListing


class OpeningView(DetailView):

    model = JobListing
    context_object_name = 'opening'
    template_name = 'shortlist/opening.html'
