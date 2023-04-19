from django import forms
from django.utils.translation import gettext_lazy as _
from shortlist.models import ShortList


STATUSES = (
    ('', 'Select'),
    ('ACCEPTED', 'QUALIFIED'),
    ('DECLINED', 'DISQUALIFIED'),
)


class UpdateShortListForm(forms.ModelForm):

    status = forms.ChoiceField(
        choices=STATUSES,
        label=_("Qualify or disqualify this application"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default', 'rows': 10}),
        required=False)

    class Meta:
        model = ShortList
        fields = ['comment']

    def __init__(self, shortlist, *args, **kwargs):
        super(UpdateShortListForm, self).__init__(*args, **kwargs)
        if shortlist:
            self.fields['comment'].initial = shortlist.comment
            self.fields['status'].initial = shortlist.application.status

    def save(self, commit=True):
        shortlist = super(UpdateShortListForm, self).save(commit=False)
        shortlist.is_reviewed = True
        status = self.cleaned_data['status']
        shortlist.application.status = status
        if status == 'ACCEPTED':
            if shortlist.application.listing.openings > 0:
                shortlist.application.listing.openings -= 1
                shortlist.application.listing.save()
        shortlist.application.save()
        if commit:
            shortlist.save()
        return shortlist
