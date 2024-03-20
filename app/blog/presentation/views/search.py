from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy


class BlogSearchView(View):

    template_name = 'pes_admin/view_applications.html'

    def get(self, request):
        search_query = request.GET.get('blog_search', None)
        if search_query:
            self.request.session['blog_search'] = search_query
        search_query = self.request.GET.get("blog_search", None)
        return redirect(reverse_lazy('blog:posts'))


class ClearBlogSearchView(View):

    template_name = 'pes_admin/view_applications.html'

    def get(self, request):
        self.request.session.pop('blog_search', None)
        return redirect(reverse_lazy('blog:posts'))
