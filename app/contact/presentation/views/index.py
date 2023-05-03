from typing import Any, Dict
from django.views.generic import TemplateView
from contact.forms import ContactEmailForm


class ContactView(TemplateView):

    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'form': ContactEmailForm})
        return context
