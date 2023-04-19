from django import forms
from django.utils.translation import gettext_lazy as _
from shortlist.models import ShortList
from accounts.models import User

SHORTLISTERS = []

try:
    SHORTLISTERS = [
        (user.pk, user)
        for user in User.objects.filter(is_staff=True).exclude(is_superuser=True)]
except Exception as e:
    print(str(e))
finally:
    SHORTLISTERS.insert(0, ('', 'Select Staff to Shortlist'))


class ShortListForm(forms.ModelForm):

    shortlister = forms.ChoiceField(
        choices=SHORTLISTERS,
        label=_("Staff"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)

    class Meta:
        model = ShortList
        fields = ['application']

    def save(self, commit=True):
        shortlist = super(ShortListForm, self).save(commit=False)
        user_pk = self.cleaned_data['shortlister']
        user = User.objects.get(pk=user_pk)
        shortlist.shortlister = user
        if commit:
            try:
                shortlist.save()
                shortlist.application.in_review = True
                shortlist.application.save()
            except ShortList.IntegrityError as ie:
                print(str(ie))
            finally:
                return shortlist
