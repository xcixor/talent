from django.views.generic import DetailView
from index.models import Service


class ServiceView(DetailView):

    template_name = 'index/service.html'
    model = Service
    context_object_name = 'service'
