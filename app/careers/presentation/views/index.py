from typing import Any
from django.utils import timezone
from django.db.models.query import QuerySet
from django.views.generic import ListView
from careers.models import Career


class IndexView(ListView):

    model = Career
    context_object_name = 'careers'
    template_name = 'careers/index.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        current_date = timezone.now()
        queryset = super().get_queryset().filter(
            application_deadline__gte=current_date,
            is_open=True)
        return queryset
