from django.db import models
from accounts.models import User
from shortlist.models import Application


SHORTLIST_STATUS = [
    ('UNASSIGNED', 'UNASSIGNED'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('ACCEPTED', 'ACCEPTED'),
    ('DECLINED', 'DECLINED'),
    ('COMPLETED', 'COMPLETED'),
]


class ShortList(models.Model):

    application = models.ForeignKey(
        Application, on_delete=models.CASCADE,
        related_name='shortlists')
    shortlister = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='shortlists')
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=40, default='UNASSIGNED',
        choices=SHORTLIST_STATUS)

    def __str__(self) -> str:
        return f"Application {str(self.id).zfill(3)} by {self.applicant}"

    class Meta:
        unique_together = ('application', 'shortlister')
