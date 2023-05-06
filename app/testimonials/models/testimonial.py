from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User


class Testimony(models.Model):

    witness = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='testimonies')
    testimony = RichTextField()

    def __str__(self) -> str:
        return f'{self.witness} - Testimony'

    class Meta:
        verbose_name_plural = 'Testimonies'
