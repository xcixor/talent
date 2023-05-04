from django.contrib import admin
from index.models import CarouselItem, Action


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):

    list_display = ['html_stripped']


admin.site.register(Action)
