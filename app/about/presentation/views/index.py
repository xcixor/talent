from django.views.generic import TemplateView
from about.models import About, Staff, Values, Partners


class AboutIndexView(TemplateView):

    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'about': About.objects.latest('-created')})
        context.update({'partners': Partners.objects.all()})
        context.update({'staff': Staff.objects.all()})
        return context
