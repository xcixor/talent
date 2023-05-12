from django.views.generic import ListView
from testimonials.models import Testimony


class TestimonialsIndexView(ListView):

    template_name = 'testimonials/index.html'
    model = Testimony
    context_object_name = 'testimonies'
    paginate_by = 5
