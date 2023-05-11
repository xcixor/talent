import logging
from django.views.generic import TemplateView
from index.models import CarouselItem, Service
from testimonials.models import Testimony
from about.models import About, Partners


logger = logging.getLogger(__name__)


class IndexView(TemplateView):

    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'carousel_items': CarouselItem.objects.all()})
        context.update({'services': Service.objects.all()})
        context.update({'testimonies': Testimony.objects.all()})
        try:
            context.update({'about': About.objects.latest('-created')})
        except About.DoesNotExist as de:
            logger.error(f'{de}')
        context.update({'partners': Partners.objects.all()})
        return context
