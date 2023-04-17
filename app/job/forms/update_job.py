from django import forms
from django.utils.translation import gettext_lazy as _
from job.models import JobListing, Industry
from job.forms.create_job import COOPERATION_TYPES, INDUSTRIES


class UpdateJobForm(forms.ModelForm):

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
    length_of_hire = forms.CharField(required=False)
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
        required=False)
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
    experience = forms.CharField(
        label="Years of experience",
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'placeholder': 'Eg. 3 years of experience in management or similar role.'}),
        required=True)

    class Meta:
        model = JobListing
        fields = [
            'title', 'description', 'requirements', 'length_of_hire',
            'proposed_remuneration', 'cooperation_type',
            'openings', 'city', 'experience']

    def __init__(self, job, *args, **kwargs):
        super(UpdateJobForm, self).__init__(*args, **kwargs)

        if job:
            print(job.experience)
            self.fields['title'].initial = job.title
            self.fields['description'].initial = job.description
            self.fields['requirements'].initial = job.requirements
            self.fields['length_of_hire'].initial = job.length_of_hire
            self.fields['proposed_remuneration'].initial = job.proposed_remuneration
            self.fields['cooperation_type'].initial = job.cooperation_type
            self.fields['industry'].initial = int(job.industry.pk)
            self.fields['openings'].initial = job.openings
            self.fields['city'].initial = job.city
            self.fields['experience'].initial = job.experience

    def save(self, commit=True):
        job = super(UpdateJobForm, self).save(commit=False)
        industry_pk = self.cleaned_data['industry']
        if industry_pk:
            industry = Industry.objects.get(pk=industry_pk)
            job.industry = industry
        if commit:
            job.save()
        return job
