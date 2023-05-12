import itertools
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from accounts.models import User


class Testimony(models.Model):

    witness = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='testimonies')
    testimony = RichTextField()
    slug = models.SlugField(
        max_length=255, unique=True,
        help_text=_('Unique address for the testimony.'))

    def _generate_slug(self):
        value = f'{self.witness.get_full_name()} {self.witness.service_type} testimony'
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Testimony.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.witness} - Testimony'

    class Meta:
        verbose_name_plural = 'Testimonies'


class BestTestimony(models.Model):

    testimony = models.OneToOneField(
        Testimony, on_delete=models.CASCADE, related_name='best')
