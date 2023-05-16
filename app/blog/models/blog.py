import itertools
from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import readtime


def image_directory_path(instance, filename):
    return (f'blog/{instance.slug}/{filename}')


class CaptionImage(models.Model):

    image = models.ImageField(upload_to=image_directory_path)


class Publication(models.Model):
    PUBLICATION_STATUSES = [
        ('draft', 'Draft'), ('publish', 'Publish'), ('archive', 'Archive')]
    author = models.CharField(
        max_length=255, null=True, blank=True, default="xcixor")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=PUBLICATION_STATUSES, default="publish")
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    epigraph = RichTextField()

    class Meta:
        abstract = True
        ordering = ['-created_on']


class Post(Publication):

    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=image_directory_path)

    def _generate_slug(self):
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Post.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    @property
    def read_time(self):
        return readtime.of_html(self.content)

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
