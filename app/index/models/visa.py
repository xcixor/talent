import itertools
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db import models
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField


def image_directory_path(instance, filename):
    return (f'services/{instance.pk}/{filename}')


class Visa(models.Model):

    title = models.CharField(max_length=40)
    description = RichTextField(null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True,
        help_text=_('Unique verbose identifier for the service.'))

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Visa.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    @property
    def html_stripped(self):
        return strip_tags(self.title)

    def __str__(self) -> str:
        return self.html_stripped
