from django.contrib import admin
from careers.models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):

    exclude = ['slug']
