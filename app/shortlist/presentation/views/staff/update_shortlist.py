from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from shortlist.models import ShortList
from shortlist.forms import UpdateShortListForm


class UpdateShortListView(UpdateView):

    model = ShortList
    form_class = UpdateShortListForm
    template_name = 'shortlist/staff/shortlists.html'
    success_url = reverse_lazy("shortlist:staff_shortlists")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(UpdateShortListView, self).get_form_kwargs()
        kwargs['shortlist'] = self.get_object()
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
