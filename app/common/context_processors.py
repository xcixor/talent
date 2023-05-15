from django.contrib.sites.shortcuts import get_current_site


def get_current_path(request):
    current_site = get_current_site(request)

    return {
        'current_full_path': f'{current_site.domain}{request.get_full_path()}'
    }
