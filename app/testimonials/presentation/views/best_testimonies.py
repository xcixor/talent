from django.views.generic import ListView
from testimonials.models import BestTestimony


class BestTestimonyView(ListView):

    template_name = 'testimonials/best.html'
    model = BestTestimony
    context_object_name = 'testimonies'
    paginate_by = 5
