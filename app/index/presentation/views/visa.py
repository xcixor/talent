from typing import Any, Dict
from django.views.generic import TemplateView
from index.models import Visa


class VisaServiceDetails(TemplateView):

    template_name = 'index/visa.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'service': Visa.objects.first()})
        return context
