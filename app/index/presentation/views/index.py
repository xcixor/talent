from typing import Any, Dict
from django.views.generic import TemplateView
from index.models import CarouselItem


class IndexView(TemplateView):

    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'carousel_items': CarouselItem.objects.all()})
        return context
