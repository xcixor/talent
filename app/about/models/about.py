from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User


def icons_directory_path(instance, filename):
    return (f'about/values/icons/{instance.pk}/{filename}')


def partners_directory_path(instance, filename):
    return (f'about/partners/{instance.pk}/{filename}')


class About(models.Model):

    version = models.IntegerField(unique=True)
    epigraph = RichTextField()
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=200)
    our_story = RichTextField()
    our_mission = RichTextField()
    our_service = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About Us Content'

    def __str__(self) -> str:
        return f'V{self.version}'


class Staff(models.Model):

    staff = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff_role')
    role = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Staff'

    def __str__(self) -> str:
        return self.staff.get_full_name()


class Values(models.Model):

    icon = models.ImageField(upload_to=icons_directory_path)
    value = models.CharField(max_length=100)
    description = RichTextField()

    class Meta:
        verbose_name_plural = 'Values'

    def __str__(self) -> str:
        return self.value


class Partners(models.Model):

    company = models.CharField(max_length=150)
    logo = models.ImageField(upload_to=partners_directory_path)

    class Meta:
        verbose_name_plural = 'Partners'

    def __str__(self) -> str:
        return self.company
