from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import User


MODE_OF_CONTACT = (
    ('', 'Select Mode of Contact'),
    ('Email', 'Email'),
    ('Whatsapp', 'Whatsapp'),
    ('Call', 'Call')
)


class UpdateModeOfContactForm(forms.ModelForm):

    mode_of_contact = forms.ChoiceField(
        choices=MODE_OF_CONTACT,
        label=_("How should we contact you"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)

    class Meta:
        model = User
        fields = ['mode_of_contact']

    def __init__(self, request, *args, **kwargs):
        super(UpdateModeOfContactForm, self).__init__(*args, **kwargs)
        user = request.user
        self.fields['mode_of_contact'].initial = user.mode_of_contact
