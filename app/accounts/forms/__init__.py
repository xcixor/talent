import re
import operator
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from django_countries.widgets import CountrySelectWidget
from common.email import HtmlEmailMixin
from accounts.tokens import account_activation_token
from phone_iso3166.country import country_prefixes
import flag
import pycountry


User = get_user_model()

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


class RegistrationForm(forms.ModelForm, HtmlEmailMixin):

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
    preferred_country = forms.ChoiceField(
        choices=get_countries("Preferred Country"),
        label=_("Preferred Country"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
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
    mode_of_contact = forms.ChoiceField(
        choices=MODE_OF_CONTACT,
        label=_("How should we contact you"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'country_code',
            'service_type', 'preferred_country', 'nationality',
            'country_of_residence', 'date_of_birth', 'gender',
            'highest_level_of_education', 'years_of_work', 'phone_number',
            'type_of_visa', 'resume', 'linkedin_url', 'mode_of_contact']

    def __init__(self, request, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        data = request.session.pop('registration_details', None)
        if data:
            self.fields['preferred_country'].choice = data['preferred_country']
            self.fields['gender'].choice = str(data['gender'])
            self.fields['service_type'].choice = data['service_type']
            self.fields['country_of_residence'].choice = data['country_of_residence']
            self.fields['nationality'].choice = data['nationality']
            self.fields['phone_number'].initial = data['phone_number']
            self.fields['first_name'].initial = data['first_name']
            self.fields['last_name'].initial = data['last_name']
            self.fields['email'].initial = data['email']
            self.fields['years_of_work'].initial = data['years_of_work']
            self.fields['linkedin_url'].initial = data['linkedin_url']
            self.fields['type_of_visa'].choice = data['type_of_visa']
            self.fields['mode_of_contact'].choice = data['mode_of_contact']
            self.fields['highest_level_of_education'].choice = data['highest_level_of_education']

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
        from_email = settings.VERIFIED_EMAIL_USER
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
        from_email = settings.VERIFIED_EMAIL_USER
        to_email = settings.ADMIN_EMAILS
        context = {
            'email_address': user.email,
            'time': timezone.now()
        }
        return super().send_email(
            subject, None, from_email, to_email,
            template='registration/email/admin/new_user.html',
            context=context)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit:
            user.save()
            # self.notify_admin(user)
        return user


class ResendActivationEmail(forms.Form, HtmlEmailMixin):

    email = forms.EmailField(required=True)

    def get_account(self, email):
        existing_user = None
        try:
            existing_user = User.objects.get(email=email)
        except User.DoesNotExist as de:
            print(de)
        return existing_user

    def clean_email(self):
        email = self.cleaned_data.get("email")
        existing_user = self.get_account(email)
        if not existing_user:
            raise forms.ValidationError(
                _("Sorry that account does not exist."), code='invalid')
        if existing_user.is_active:
            raise forms.ValidationError(
                _(
                    'Your account is already active. '
                    'Please login with the details you registered with, '
                    'or reset your password'), code='invalid')
        return email

    def resend_account_activation_email(self, request):
        email = self.cleaned_data.get("email")
        user = self.get_account(email)
        if not user:
            raise forms.ValidationError(
                _("Sorry the account does not exist."), code='invalid')
        to_email = user.email
        subject = _("Welcome to Agripitch 2022!")
        from_email = settings.VERIFIED_EMAIL_USER
        current_site = get_current_site(request)
        context = {
            "username": user.username,
            "email": user.email,
            'domain': current_site.domain,
            "protocol": request.scheme,
            'email_head': subject,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        }
        return super().send_email(
            subject, None, from_email, [to_email],
            template='registration/email/account_activation.html',
            context=context)

    def notify_admin(self, user):
        subject = _(
            'New User Registration')
        from_email = settings.VERIFIED_EMAIL_USER
        to_email = settings.ADMIN_EMAILS
        context = {
            'email_address': user.email,
            'time': timezone.now()
        }
        return super().send_email(
            subject, None, from_email, to_email,
            template='registration/email/admin/new_user.html',
            context=context)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_active = True
            user.save()
        # if not settings.DEBUG:
        #     self.notify_admin(user)
        return user


class LoginForm(AuthenticationForm):

    remember_me = forms.BooleanField(required=False)
