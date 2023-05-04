from django.db import models
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField


class CarouselItem(models.Model):

    title = RichTextField()
    subtitle = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    @property
    def html_stripped(self):
        return strip_tags(self.title)


class Action(models.Model):

    carousel_item = models.ForeignKey(
        CarouselItem, on_delete=models.CASCADE, related_name='actions')
    title = models.CharField(max_length=40)
    link = models.URLField()

    def __str__(self) -> str:
        return self.link
