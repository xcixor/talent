from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from accounts.forms.utils import get_phone_codes
from common.email import HtmlEmailMixin


class ContactEmailForm(forms.Form, HtmlEmailMixin):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    country_code = forms.IntegerField()
    phone_number = forms.IntegerField()
    country_code = forms.ChoiceField(
        choices=get_phone_codes(),
        label=_("Country Code"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    subject = forms.CharField(max_length=400)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        """Send contact us email

        Returns:
            bool: status of email send
        """
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        message = self.cleaned_data['message']
        phone_number = self.cleaned_data['phone_number']
        country_code = self.cleaned_data['country_code']
        phone_number = f'{phone_number}{country_code}'
        from_email = settings.EMAIL_HOST_USER
        context = {
            "first_name": first_name,
            "email": email,
            'last_name': last_name,
            "message": message,
            'email_head': subject,
            'phone_number': phone_number
        }
        return super().send_email(
            subject, None, from_email, [from_email],
            template='email/contact.html',
            context=context)
