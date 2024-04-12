from itertools import chain
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from job.models import JobListing, Industry


class OpeningsView(ListView):

    model = JobListing
    context_object_name = 'openings'
    template_name = 'shortlist/openings.html'
    partial_template_name = 'shortlist/partials/openings.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        sort_term = self.request.GET.get('sort', None)
        if sort_term:
            self.request.session['sort'] = sort_term
        search_term = self.request.GET.get('search', None)
        if search_term:
            self.request.session['search'] = search_term
        return super().get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        sort_term = self.request.session.get('sort', None)
        if sort_term:
            industry = Industry.objects.get(pk=int(sort_term))
            queryset = queryset.filter(industry=industry)

        search_fields = \
            SearchVector('industry__title') \
            + SearchVector('industry__description') \
            + SearchVector('title') \
            + SearchVector('description') \
            + SearchVector('proposed_remuneration') \
            + SearchVector('city') \
            + SearchVector('cooperation_type')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'industries': Industry.objects.all()})
        return context

    def get_template_names(self):
        print(self.request.htmx)
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name
