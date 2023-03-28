from django.urls import path
from backup.presentation.views import BackupView

app_name = 'backup'

urlpatterns = [
    path('', BackupView.as_view(), name='backup')
]
