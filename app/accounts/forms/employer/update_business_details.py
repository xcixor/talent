import operator
from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from phone_iso3166.country import country_prefixes
import flag
import pycountry
from accounts.models import CompanyDetails


def get_countries(placeholder):
    countries = []
    countries.append(('', placeholder))
    prefixes = country_prefixes()
    sorted_dict = sorted(prefixes.items(), key=operator.itemgetter(0))
    for item in sorted_dict:
        country = pycountry.countries.get(alpha_2=item[0])
        if country:
            phone_tuple = (
                country.name, f'{flag.flag(item[0])} {country.name}'
            )
            countries.append(phone_tuple)
    return countries


class UpdateBusinessInfoForm(forms.ModelForm):

    country = forms.ChoiceField(
        choices=get_countries("Country of residence"),
        label=_("Where do you currently reside"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    company_name = forms.CharField(
        label=_("Company Name *"),
        widget=forms.TextInput(
            attrs={
                'class': 'validate'}),)
    tax_number = forms.IntegerField(
        label='NIP (tax number) *',
        widget=forms.NumberInput(
            attrs={
                'class': 'validate'}), required=False)
    address_line_one = forms.CharField(required=False)
    address_line_two = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)

    class Meta:
        model = CompanyDetails
        fields = [
            'company_name', 'tax_number', 'address_line_one',
            'address_line_two', 'city', 'state', 'postal_code',
            'country']

    def __init__(self, request, *args, **kwargs):
        super(UpdateBusinessInfoForm, self).__init__(*args, **kwargs)
        user = request.user
        self.fields['company_name'].initial = user.company.company_name
        self.fields['country'].initial = user.company.country
        self.fields['tax_number'].initial = user.company.tax_number
        self.fields['address_line_one'].initial = user.company.address_line_one
        self.fields['address_line_two'].initial = user.company.address_line_two
        self.fields['city'].initial = user.company.city
        self.fields['state'].initial = user.company.state
        self.fields['postal_code'].initial = user.company.postal_code
