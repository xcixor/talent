from django.views.generic import TemplateView


class AboutIndexView(TemplateView):

    template_name = 'about/index.html'
