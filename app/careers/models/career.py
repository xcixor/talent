import itertools
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Career(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255, unique=True,
        help_text=_('Unique address for the testimony.'))
    description = RichTextField()
    created = models.DateField(auto_now=True)
    is_open = models.BooleanField(
        verbose_name=_('Open for Applications?'), default=True)
    application_deadline = models.DateTimeField(
        verbose_name=_('When the applications close'))

    def _generate_slug(self):
        value = f'{self.title}'
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Career.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title}'
