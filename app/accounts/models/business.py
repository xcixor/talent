from django.db import models
from accounts.models import User


class CompanyDetails(models.Model):

    company_owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(max_length=400)
    tax_number = models.IntegerField(blank=True, null=True)
    address_line_one = models.CharField(max_length=400, blank=True, null=True)
    address_line_two = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=400, blank=True, null=True)
    state = models.CharField(max_length=400, blank=True, null=True)
    postal_code = models.CharField(max_length=400, blank=True, null=True)
    country = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self) -> str:
        return self.company_name

    class Meta:

        verbose_name_plural = 'Company Details'
