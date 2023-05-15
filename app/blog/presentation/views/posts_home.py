from itertools import chain
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from blog.models import Post


class PostsHomeView(ListView):

    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_base.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs).filter(status='publish')
        search_fields = \
            SearchVector('title') \
            + SearchVector('epigraph') \
            + SearchVector('content')
        search_query = self.request.session.get('blog_search', None)
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
        print(queryset, 'searching...')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
