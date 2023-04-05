from django.views.generic.edit import DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy
from job.models import JobListing


class DeleteJobListingView(DeleteView):

    template_name = 'job/jobs.html'
    model = JobListing
    context_object_name = 'job'
    success_url = reverse_lazy('job:view_jobs')

    def get_success_url(self):
        success_message = _('Great, the job has been deleted.')
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().get_success_url()

    def form_invalid(self, form):
        print(form.errors.as_data())
        error_message = _('Hmm, that didn\'t work please try again.')
        messages.add_message(
            self.request, messages.ERROR, error_message)
        return super().form_invalid(form)
