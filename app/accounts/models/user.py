from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CharField
max_length = 255


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email, and password.
        """
        if not username:
            raise ValueError(_('A User must have a username'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_temporal_user(self, email, **extra_fields):
        user = self.model(email=email, username=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(username, password, **extra_fields)

    def get_user_by_uid(self, uidb64):
        """
        Return a user object based on the user's id encoded in base 64.
        """
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = self.get_queryset().get(pk=uid)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
            user = None
        return user


def image_directory_path(instance, filename):
    return (f'accounts/{instance.email}/{filename}')


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=40, unique=True, blank=True, null=True)
    email = models.EmailField(
        verbose_name=_('Email Address'), max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True, max_length=20)
    gender = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(
        upload_to=image_directory_path, null=True, blank=True)
    resume = models.FileField(
        upload_to=image_directory_path)
    phone_number = models.IntegerField()
    years_of_work = models.IntegerField()
    country_code = models.CharField(max_length=255)
    preferred_country = CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    preferred_country = CharField(max_length=255)
    nationality = CharField(max_length=255)
    country_of_residence = CharField(max_length=255)
    highest_level_of_education = models.CharField(max_length=255)
    type_of_visa = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=255)
    mode_of_contact = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self) -> str:
        return 'STAFF-ID-' + str(self.id).zfill(3)

    class Meta:
        ordering = ['date_joined']
