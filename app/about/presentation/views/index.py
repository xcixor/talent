import logging
from django.views.generic import TemplateView
from about.models import About, Staff, Values, Partners
from index.models import Service


logger = logging.getLogger(__name__)


class AboutIndexView(TemplateView):

    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context.update({'about': About.objects.latest('-created')})
        except About.DoesNotExist as de:
            logger.error(f'{de}')
        context.update({'partners': Partners.objects.all()})
        context.update({'staff': Staff.objects.all()})
        context.update({'services': Service.objects.all()})
        return context
