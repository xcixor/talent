from django import forms
from django.utils.translation import gettext_lazy as _
from job.models import JobListing, Industry

COOPERATION_TYPES = (
    ('Leasing of employees on the basis of the law on temporary work',
     'Leasing of employees on the basis of the law on temporary work'),
    ('Selection of personnel - (conducting recruitment for the client, and then handing over candidates for a one-time fee)',
     'Selection of personnel - (conducting recruitment for the client, and then handing over candidates for a one-time fee)'),
    ('Temporary work - (Hiring of personnel based on the Act on Temporary Work and entrusting the client with management supervision)',
     'Temporary work - (Hiring of personnel based on the Act on Temporary Work and entrusting the client with management supervision)'),
)

INDUSTRIES = []
try:
    INDUSTRIES = [(industry.pk, industry) for industry in Industry.objects.all()]
except Exception as e:
    print(str(e))
finally:
    INDUSTRIES.insert(0, ('', 'Select the Industry'))


class CreateJobForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'validate'}), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'validate', 'rows': '5'}), required=True)
    requirements = forms.CharField(
        label="What are the job requirements (experience, skills, certificates) *",
        widget=forms.Textarea(attrs={'rows': '5'}),
        required=True)
    length_of_hire = forms.CharField(
        required=False, label="How long will the job last?")
    proposed_remuneration = forms.CharField(
        required=False,
        label=_("Proposed Remuneration in USD"),
    )
    cooperation_type = forms.ChoiceField(
        choices=COOPERATION_TYPES,
        label=_("What type of cooperation would you like with our agency?"),
        widget=forms.RadioSelect(
            attrs={
                'class': 'show_select browser-default'}),
        required=False)
    industry = forms.ChoiceField(
        choices=INDUSTRIES,
        label=_("Job Industry"),
        widget=forms.Select(
            attrs={
                'class': 'show_select browser-default'}),
        required=True)
    terms = forms.BooleanField(initial=False, required=True)
    city = forms.CharField(
        label="Which city will they be working?",
        widget=forms.TextInput(attrs={
            'class': 'validate'}),
        required=True)
    openings = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'validate'}),
        label="How many posts are there?",
        required=True)

    class Meta:
        model = JobListing
        fields = [
            'title', 'description', 'requirements', 'length_of_hire',
            'proposed_remuneration', 'cooperation_type',
            'openings', 'city']

    def __init__(self, request, *args, **kwargs):
        super(CreateJobForm, self).__init__(*args, **kwargs)
        self.user = request.user
        data = request.session.pop('job_data', None)
        if data:
            self.fields['title'].initial = data.get('title', "")
            self.fields['description'].initial = data.get('description', "")
            self.fields['requirements'].initial = data.get('requirements', "")
            self.fields['length_of_hire'].initial = data.get(
                'length_of_hire', "")
            self.fields['proposed_remuneration'].initial = data.get(
                'proposed_remuneration', "")
            self.fields['cooperation_type'].initial = data.get(
                'cooperation_type', "")

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        job.job_owner = self.user
        industry_pk = self.cleaned_data['industry']
        industry = Industry.objects.get(pk=industry_pk)
        job.industry = industry
        if commit:
            job.save()
        return job
