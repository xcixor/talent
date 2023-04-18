from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from shortlist.models import ShortList


class StaffApplications(LoginRequiredMixin, ListView):

    model = ShortList
    template_name = 'shortlist/staff/applications.html'
    context_object_name = 'applications'
    partial_template_name = 'shortlist/staff/partials/applications.html'
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
        queryset = super().get_queryset(**kwargs).filter(
            shortlister=self.request.user)
        search_fields = \
            SearchVector('application__listing__industry__title') \
            + SearchVector('application__listing__industry__description') \
            + SearchVector('application__listing__title') \
            + SearchVector('application__listing__description') \
            + SearchVector('application__listing__proposed_remuneration') \
            + SearchVector('application__listing__city')
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
        print(self.request.htmx)
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name
