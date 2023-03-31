import operator
from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from phone_iso3166.country import country_prefixes
import flag
import pycountry
from accounts.models import User
from common.email import HtmlEmailMixin

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


class UpdateBasicInfoForm(forms.ModelForm, HtmlEmailMixin):

    nationality = forms.ChoiceField(
        choices=get_countries("Nationality"),
        label=_("Nationality"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    country_of_residence = forms.ChoiceField(
        choices=get_countries("Country of residence"),
        label=_("Where do you currently reside"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    highest_level_of_education = forms.ChoiceField(
        choices=LEVEL_OF_EDUCATION,
        label=_("Highest Level of Education"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    type_of_visa = forms.ChoiceField(
        choices=TYPE_OF_VISA,
        label=_("Your current type of Visa"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    years_of_work = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'validate'}), required=True)
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'datepicker'}), required=True, input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = [
            'nationality', 'country_of_residence', 'date_of_birth',
            'highest_level_of_education', 'years_of_work', 'type_of_visa']

    def __init__(self, request, *args, **kwargs):
        super(UpdateBasicInfoForm, self).__init__(*args, **kwargs)
        user = request.user
        self.fields['nationality'].initial = user.nationality
        self.fields['country_of_residence'].initial = user.country_of_residence
        self.fields['date_of_birth'].initial = user.date_of_birth.strftime(
            "% m/%d/%Y")

        self.fields['highest_level_of_education'].initial = user.highest_level_of_education
        self.fields['years_of_work'].initial = user.years_of_work
        self.fields['type_of_visa'].initial = user.type_of_visa
