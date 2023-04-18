from django.views.generic.edit import CreateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from shortlist.forms import ShortListForm
from shortlist.models import ShortList, Application


class CreateShortListView(CreateView):

    model = ShortList
    form_class = ShortListForm
    template_name = 'infinite_admin/applications/create_shortlist.html'
    success_url = reverse_lazy("basic_admin:unassigned_applications")

    def get(self, request, *args, **kwargs):
        self.application = Application.objects.get(pk=kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application'] = self.application
        return context

    def form_valid(self, form):
        success_message = _("Application assigned successfully.")
        messages.add_message(
            self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        success_message = _("Something went wrong.")
        messages.add_message(
            self.request, messages.ERROR, success_message)
        return super().form_invalid(form)
