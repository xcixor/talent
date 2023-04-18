from django import forms
from shortlist.models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['listing']

    def __init__(self, request, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.user = request.user

    def save(self, commit=True):
        application = super(ApplicationForm, self).save(commit=False)
        application.applicant = self.user
        if commit:
            try:
                application.save()
            except Application.IntegrityError as ie:
                print(str(ie))
            finally:
                return application
