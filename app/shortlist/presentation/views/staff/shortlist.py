from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.urls import reverse_lazy
from shortlist.models import ShortList
from shortlist.forms import UpdateShortListForm


class ShortListView(PermissionRequiredMixin, DetailView):

    model = ShortList
    template_name = 'shortlist/staff/shortlist.html'
    permission_required = ('shortlist.can_view_shortlist', )
    permission_denied_message = _(
        'Hmm it seems that you cannot review this application '
        'please contact your admin.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form': UpdateShortListForm(self.get_object())})
        return context

    def handle_no_permission(self):
        messages.add_message(
            self.request, messages.ERROR, self.permission_denied_message)
        return redirect(reverse_lazy('shortlist:staff_shortlists'))
