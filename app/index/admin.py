from django.contrib import admin
from index.models import CarouselItem, Action, Service, Visa


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):

    list_display = ['html_stripped']


@admin.register(Visa)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ['slug']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(Action)
