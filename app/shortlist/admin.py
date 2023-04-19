from django.contrib import admin
from shortlist.models import Application, ShortList


@admin.register(ShortList)
class ShortListAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
