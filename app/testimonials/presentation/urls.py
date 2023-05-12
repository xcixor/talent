from django.urls import path
from testimonials.presentation.views import TestimonialsIndexView, TestimonialView
app_name = 'testimonials'

urlpatterns = [
    path('', TestimonialsIndexView.as_view(), name='index'),
    path('testimonial/<slug:slug>/', TestimonialView.as_view(), name='testimonial')
]
