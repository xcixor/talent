from django.db import models
from accounts.models import User
from job.models import JobListing


SHORTLIST_STATUS = [
    ('UNASSIGNED', 'UNASSIGNED'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('ACCEPTED', 'ACCEPTED'),
    ('DECLINED', 'DECLINED'),
    ('COMPLETED', 'COMPLETED'),
]


class Application(models.Model):

    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='applications')
    listing = models.ForeignKey(
        JobListing, on_delete=models.CASCADE,
        related_name='applications')
    created = models.DateTimeField(auto_now=True)
    in_review = models.BooleanField(default=False)
    status = models.CharField(
        max_length=40, default='UNASSIGNED',
        choices=SHORTLIST_STATUS)

    def __str__(self) -> str:
        return f"Application {str(self.pk).zfill(3)} by {self.applicant}"

    class Meta:
        unique_together = ('applicant', 'listing')
