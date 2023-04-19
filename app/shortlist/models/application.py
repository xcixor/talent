from django.db import models
from accounts.models import User
from job.models import JobListing


class Application(models.Model):

    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='applications')
    listing = models.ForeignKey(
        JobListing, on_delete=models.CASCADE,
        related_name='applications')
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    in_review = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Application {str(self.pk).zfill(3)} by {self.applicant}"

    class Meta:
        unique_together = ('applicant', 'listing')
