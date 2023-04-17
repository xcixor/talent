from itertools import chain
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from job.models import JobListing, Industry


class IndustryOpeningsView(ListView):

    model = JobListing
    context_object_name = 'openings'
    template_name = 'shortlist/industry_openings.html'
    partial_template_name = 'shortlist/partials/industry_openings.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        search_term = self.request.GET.get('search')
        if search_term:
            self.request.session['search'] = search_term
        return super().get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        industry = Industry.objects.get(slug=self.slug)
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
        context.update({'industry': Industry.objects.get(slug=self.slug)})
        return context

    def get_template_names(self):
        print(self.request.htmx)
        if self.request.htmx:
            return self.partial_template_name
        return self.template_name
