from django.views.generic import DetailView
from index.models import Visa


class VisaServiceDetails(DetailView):

    model = Visa
    template_name = 'index/visa.html'
    context_object_name = 'service'
