from django.contrib.sites.shortcuts import get_current_site
from index.models import Service


def get_current_path(request):
    current_site = get_current_site(request)

    return {
        'current_full_path': f'{current_site.domain}{request.get_full_path()}'
    }


def services(request):
    """Provides service model objects for the django context

    Args:
        request (object): _description_

    Returns:
        object: A queryset of service model objects
    """
    return {'services': Service.objects.all()}
