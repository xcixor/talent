from django.views.generic import DetailView
from testimonials.models import Testimony


class TestimonialView(DetailView):

    template_name = 'testimonials/testimonial.html'
    model = Testimony
    context_object_name = 'testimony'
