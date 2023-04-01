from django import forms
from accounts.models import User


class UpdateResumeForm(forms.ModelForm):

    linkedin_url = forms.URLField(widget=forms.URLInput(), required=False)
    resume = forms.FileField(widget=forms.ClearableFileInput(
        attrs={
            'class': 'validate', 'accept': '.pdf'}), required=True)

    class Meta:
        model = User
        fields = [
            'resume', 'linkedin_url']

    def __init__(self, request, *args, **kwargs):
        super(UpdateResumeForm, self).__init__(*args, **kwargs)
        user = request.user
        self.fields['linkedin_url'].initial = user.linkedin_url
        self.fields['resume'].initial = user.resume
