from django.contrib import admin
from testimonials.models import Testimony


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):

    exclude = ['slug']
    list_display = ['__str__', 'slug']
