from django.views.generic.edit import UpdateView
from django.views import View
from django.views.generic import DetailView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from job.forms import UpdateJobForm
from job.models import JobListing


class GetUpdateJobView(DetailView):

    template_name = 'job/change_job_info.html'
    model = JobListing
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UpdateJobForm(self.get_object())
        return context


class PostUpdateJobView(UpdateView):

    model = JobListing
    form_class = UpdateJobForm
    template_name = 'job/change_job_info.html'
    success_url = reverse_lazy("job:view_jobs")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(PostUpdateJobView, self).get_form_kwargs()
        kwargs['job'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        success_message = _("Update successful.")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        success_message = _("Something went wrong.")
        messages.add_message(
            self.request, messages.ERROR, success_message)
        return super().form_invalid(form)


class UpdateJobView(View):

    def get(self, request, *args, **kwargs):
        view = GetUpdateJobView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostUpdateJobView.as_view()
        return view(request, *args, **kwargs)
