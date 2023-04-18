from django import template
from shortlist.models import Application

register = template.Library()


@register.filter(name="is_applied_to")
def is_applied_to(opening, user):
    applied_to = None
    try:
        applied_to = Application.objects.filter(
            applicant=user, listing=opening)
    except Application.DoesNotExist as de:
        print(de)
    return applied_to
