import re
import operator
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from phone_iso3166.country import country_prefixes
import flag
import pycountry
from captcha.fields import ReCaptchaField
from common.email import HtmlEmailMixin
from accounts.models import CompanyDetails


User = get_user_model()


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


class EmployerRegistrationForm(forms.ModelForm, HtmlEmailMixin):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    terms = forms.BooleanField(initial=False, required=True)
    captcha = ReCaptchaField(required=True)
    country_code = forms.ChoiceField(
        choices=get_phone_codes(),
        label=_("Country Code"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    country = forms.ChoiceField(
        choices=get_countries("Country"),
        label=_("Country"),
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
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'country_code', 'phone_number']

    def __init__(self, request, *args, **kwargs):
        super(EmployerRegistrationForm, self).__init__(*args, **kwargs)
        data = request.session.pop('registration_details', None)
        if data:
            self.fields['phone_number'].initial = data.get('phone_number', "")
            self.fields['first_name'].initial = data.get('first_name', "")
            self.fields['last_name'].initial = data.get('last_name', "")
            self.fields['email'].initial = data.get('email', "")

    def clean_password1(self):
        password = self.cleaned_data['password1']
        validate_password(password)
        self.custom_validate_password(password)
        return password

    def clean_terms(self):
        terms = self.cleaned_data['terms']
        if not terms:
            terms_error_message = _(
                'Please read and agree to our terms '
                'and privacy by checking the box')
            raise forms.ValidationError(terms_error_message)
        return terms

    def custom_validate_password(self, password):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not regex.search(password):
            raise forms.ValidationError(
                _("Your password should have a special character."))
        if not any(i.isdigit() for i in password):
            raise forms.ValidationError(
                _("Your password should have at least one number."))
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("Please make sure your passwords match."))
        return password2

    def send_account_creation_notification(self, user, request):
        to_email = user.email
        subject = _("Account Creation Successful!")
        from_email = settings.EMAIL_HOST_USER
        current_site = get_current_site(request)
        context = {
            "first_name": user.first_name,
            "email": user.email,
            'domain': current_site.domain,
            "protocol": request.scheme,
            'email_head': subject
        }
        return super().send_email(
            subject, None, from_email, [to_email],
            template='accounts/registration/email/account_created.html',
            context=context)

    def notify_admin(self, user):
        subject = _(
            'New User Registration')
        from_email = settings.EMAIL_HOST_USER
        to_email = settings.ADMIN_EMAILS
        context = {
            'email_address': user.email,
            'time': timezone.now()
        }
        return super().send_email(
            subject, None, from_email, to_email,
            template='registration/email/admin/new_user.html',
            context=context)

    def save_business_details(self, owner):
        business = CompanyDetails.objects.create(
            company_owner=owner,
            company_name=self.cleaned_data['company_name'],
            tax_number=self.cleaned_data['tax_number'],
            address_line_one=self.cleaned_data['address_line_one'],
            address_line_two=self.cleaned_data['address_line_two'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            postal_code=self.cleaned_data['postal_code'],
            country=self.cleaned_data['country'],
        )
        business.save()

    def save(self, commit=True):
        user = super(EmployerRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.type_of_user = 'EMPLOYER'
        if commit:
            user.save()
            self.save_business_details(user)
            # self.notify_admin(user)
        return user
