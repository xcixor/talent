import operator
from django import forms
from django.utils.translation import gettext_lazy as _
from phone_iso3166.country import country_prefixes
import flag
import pycountry
from accounts.models import User


GENDER_CHOICES = (
    ('', 'Choose your Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('I would rather not say', 'I would rather not say'),
)

SERVICE_TYPES = (
    ('', 'Select Service Type'),
    ('Sales and Marketing', 'Sales and Marketing'),
    ('Power Plant', 'Power Plant'),
    ('Agricultural', 'Agricultural'),
    ('Automotive', 'Automotive'),
    ('Food', 'Food')
)

LEVEL_OF_EDUCATION = (
    ('', 'Select Highest Level of Education'),
    ('High School', 'High School'),
    ('Diploma', 'Diploma'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
)

TYPE_OF_VISA = (
    ('', 'Select Type of Visa'),
    ('Not Applicable', 'High School'),
    ('Student Visa', 'Student Visa'),
    ('Tourist Visa', 'Tourist Visa'),
    ('Family Visa', 'Family Visa'),
    ('General Visa', 'General Visa'),
)

MODE_OF_CONTACT = (
    ('', 'Select Mode of Contact'),
    ('Email', 'Email'),
    ('Whatsapp', 'Whatsapp'),
    ('Call', 'Call')
)


def get_phone_codes():
    phone_codes = []
    phone_codes.append(('254', f"{flag.flag('KE')} Kenya +254"))
    prefixes = country_prefixes()
    sorted_dict = sorted(prefixes.items(), key=operator.itemgetter(0))
    for item in sorted_dict:
        country = pycountry.countries.get(alpha_2=item[0])
        if country:
            phone_tuple = (
                item[1], f'{flag.flag(item[0])} {country.name} +{item[1]}'
            )
            phone_codes.append(phone_tuple)
    return phone_codes


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


class UpdatePersonalInfoForm(forms.ModelForm):

    country_code = forms.ChoiceField(
        choices=get_phone_codes(),
        label=_("Country Code"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    preferred_country = forms.ChoiceField(
        choices=get_countries("Preferred Country"),
        label=_("Preferred Country"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label=_("Gender"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    service_type = forms.ChoiceField(
        choices=SERVICE_TYPES,
        label=_("Service Type"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'validate'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'validate'}), required=True)
    phone_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'validate'}), required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'gender',
            'country_code', 'phone_number', 'service_type',
            'preferred_country']

    def __init__(self, request, *args, **kwargs):
        super(UpdatePersonalInfoForm, self).__init__(*args, **kwargs)
        user = request.user
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['country_code'].initial = user.country_code
        self.fields['gender'].initial = user.gender
        self.fields['service_type'].initial = user.service_type
        self.fields['preferred_country'].initial = user.preferred_country
        self.fields['country_code'].initial = user.country_code
