from django.db import models
from accounts.models import User
from shortlist.models import Application


class ShortList(models.Model):

    application = models.ForeignKey(
        Application, on_delete=models.CASCADE,
        related_name='shortlists')
    shortlister = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='shortlists')
    created = models.DateTimeField(auto_now=True)
    is_reviewed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{str(self.id).zfill(3)} In review by {self.shortlister}"

    class Meta:
        unique_together = ('application', 'shortlister')
        ordering = ['created']
