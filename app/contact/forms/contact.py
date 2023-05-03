from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.forms.utils import get_countries


class ContactEmailForm(forms.Form):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    phone_number = forms.IntegerField()
    country = forms.ChoiceField(
        choices=get_countries("Select Country"),
        label=_("Select Country"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    subject = forms.CharField(max_length=400)
    message = forms.CharField(widget=forms.Textarea)
