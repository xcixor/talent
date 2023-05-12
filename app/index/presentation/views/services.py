from django.views.generic import DetailView, ListView
from index.models import Service


class ServiceView(DetailView):

    template_name = 'index/service.html'
    model = Service
    context_object_name = 'service'


class ServiceIndexView(ListView):

    template_name = 'index/services.html'
    model = Service
    context_object_name = 'services'
