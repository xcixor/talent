from django.urls import path
from testimonials.presentation.views import TestimonialsIndexView
app_name = 'testimonials'

urlpatterns = [
    path('', TestimonialsIndexView.as_view(), name='index')
]
