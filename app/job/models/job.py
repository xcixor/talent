from django.db import models
from accounts.models import User


class Industry(models.Model):

    title = models.CharField(
        max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name_plural = 'Job Categories'


class JobListing(models.Model):

    industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE, related_name='openings')
    job_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='job')
    title = models.CharField(
        max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    length_of_hire = models.CharField(max_length=200, blank=True, null=True)
    proposed_remuneration = models.CharField(
        max_length=400, blank=True, null=True)
    cooperation_type = models.CharField(
        max_length=400, blank=True, null=True)
    openings = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name_plural = 'Job Listing'
        ordering = ['industry']
