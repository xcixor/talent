from django.views.generic import DetailView
from careers.models import Career


class CareerView(DetailView):

    template_name = 'careers/career.html'
    model = Career
    context_object_name = 'career'
