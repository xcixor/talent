from django.db import models
from accounts.models import User


class JobCategory(models.Model):

    title = models.CharField(
        max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name_plural = 'Job Categories'


class JobListing(models.Model):

    category = models.ForeignKey(
        JobCategory,
        on_delete=models.CASCADE, related_name='openings')
    job_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='job')
    title = models.CharField(
        max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    length_of_hire = models.IntegerField(blank=True, null=True)
    proposed_remuneration = models.CharField(
        max_length=400, blank=True, null=True)
    cooperation_type = models.CharField(
        max_length=400, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name_plural = 'Job Listing'
