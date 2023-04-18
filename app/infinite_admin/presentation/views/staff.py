from itertools import chain
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from accounts.models import User


class StaffView(ListView):

    model = User
    context_object_name = 'users'
    template_name = 'infinite_admin/staff.html'
    partial_template_name = 'infinite_admin/partials/staff.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        sort_term = self.request.GET.get('sort')
        if sort_term:
            self.request.session['sort'] = sort_term
        search_term = self.request.GET.get('search')
        if search_term:
            self.request.session['search'] = search_term
        return super().get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs).filter(is_staff=True)
        search_fields = \
            SearchVector('first_name') \
            + SearchVector('last_name') \
            + SearchVector('email') \
            + SearchVector('id') \
            + SearchVector('phone_number')
        search_query = self.request.session.get('search', None)
        if search_query:
            full_search = queryset.annotate(
                search=search_fields
            ).filter(search=search_query)
            partial_search = queryset.annotate(
                search=search_fields
            ).filter(search__icontains=search_query)
            search_results = list(chain(full_search, partial_search))
            search_results = list(set(search_results))
            queryset = search_results
        return queryset

    def get_template_names(self):
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name
