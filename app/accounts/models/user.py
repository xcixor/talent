from datetime import date
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

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError(_('A User must have an email.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_temporal_user(self, email, **extra_fields):
        user = self.model(email=email, username=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, **extra_fields)

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

    USER_TYPES = (
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('EMPLOYER', 'Employer'),
        ('JOB_SEEKER', 'Job Seeker')
    )

    username = models.CharField(
        max_length=40, unique=True, blank=True, null=True)
    email = models.EmailField(
        verbose_name=_('Email Address'), max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True, max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=image_directory_path, null=True, blank=True)
    resume = models.FileField(
        upload_to=image_directory_path)
    phone_number = models.IntegerField(blank=True, null=True)
    years_of_work = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    preferred_country = CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=255, blank=True, null=True)
    preferred_country = CharField(max_length=255, blank=True, null=True)
    nationality = CharField(max_length=255, blank=True, null=True)
    country_of_residence = CharField(max_length=255, blank=True, null=True)
    highest_level_of_education = models.CharField(
        max_length=255, blank=True, null=True)
    type_of_visa = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255)
    mode_of_contact = models.CharField(max_length=255, blank=True, null=True)
    type_of_user = models.CharField(max_length=255, choices=USER_TYPES)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'type_of_user']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_formatted_phone_number(self):
        return f'+{self.country_code} {self.phone_number}'

    def get_short_name(self):
        return self.username

    def get_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - \
            ((today.month, today.day) <
             (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self) -> str:
        if self.is_superuser:
            return 'ADMIN-ID-' + str(self.pk).zfill(1)
        if self.is_staff:
            return 'STAFF-ID-' + str(self.pk).zfill(1)
        return 'ITL-ID-' + str(self.pk).zfill(3)

    class Meta:
        ordering = ['date_joined']
