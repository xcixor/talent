from django.contrib import admin
from index.models import CarouselItem, Action, Service


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):

    list_display = ['html_stripped']


admin.site.register(Action)
admin.site.register(Service)
