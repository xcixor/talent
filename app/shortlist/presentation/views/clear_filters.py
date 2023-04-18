from django_htmx.http import HttpResponseClientRedirect
from django.views.generic import View


class ClearFiltersView(View):

    template_name = 'pes_admin/view_applications.html'

    def get(self, request, *args, **kwargs):
        filter_param = kwargs.get('filter_param', None)
        if filter_param == 'search':
            print(self.request.session.pop('search', None))
        elif filter_param == 'sort':
            self.request.session.pop('sort', None)
        next = kwargs.get('next', None)
        return HttpResponseClientRedirect(next)
