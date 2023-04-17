from django.views.generic import DetailView
from job.models import JobListing


class OpeningView(DetailView):

    model = JobListing
    context_object_name = 'opening'
    template_name = 'shortlist/opening.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        opening = self.get_object()
        similar = JobListing.objects.filter(
            industry=opening.industry).exclude(pk=opening.pk)[:3]
        context['similar'] = similar
        return context
