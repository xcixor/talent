from django.views.generic.edit import CreateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from job.forms import CreateJobForm
from job.models import JobListing


class CreateJobView(CreateView):

    model = JobListing
    form_class = CreateJobForm
    template_name = 'job/create_job.html'
    success_url = reverse_lazy("job:view_jobs")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(CreateJobView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.request.session.pop('job_data', None)
        success_message = _("Job posted successfully.")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        job_data = {}
        for key, value in self.request.POST.items():
            job_data[key] = value
        self.request.session['job_data'] = job_data
        success_message = _("Something went wrong.")
        messages.add_message(
            self.request, messages.ERROR, success_message)
        return super().form_invalid(form)
