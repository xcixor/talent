from django.views import View
from django.views.generic.edit import SingleObjectMixin
from django.shortcuts import render
from accounts.models import User


class PermissionsView(View, SingleObjectMixin):

    model = User
    template_name = 'infinite_admin/permissions.html'

    def get(self, request, *args, **kwargs):
        context = {'user': self.get_object()}
        return render(request, self.template_name, context)
