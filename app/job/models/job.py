import itertools
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db import models
from accounts.models import User


class Industry(models.Model):

    title = models.CharField(
        max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True,
        help_text=_('Unique address for the industry.'))

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Industry.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

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
    slug = models.SlugField(
        max_length=255, unique=True,
        help_text=_('Unique address for the opening.'))
    created = models.DateTimeField(auto_now=True)
    experience = models.CharField(max_length=200, blank=True, null=True)

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not JobListing.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:

        verbose_name_plural = 'Job Listing'
        ordering = ['industry']
        unique_together = (('job_owner', 'title', 'city'))
