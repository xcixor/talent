from django.urls import path
from testimonials.presentation.views import (
    TestimonialsIndexView, TestimonialView, BestTestimonyView)
app_name = 'testimonials'

urlpatterns = [
    path('', TestimonialsIndexView.as_view(), name='index'),
    path('best/', BestTestimonyView.as_view(), name='best_testimonies'),
    path('testimonial/<slug:slug>/', TestimonialView.as_view(), name='testimonial')
]
