from django import forms
from django.contrib.auth.forms import UserCreationForm
from first.models import *
class UserRForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ['usertype','username','password1','password2']

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['email','company_name']


class SeekerForm(forms.ModelForm):
    looking_job_in = forms.MultipleChoiceField(choices=(("Mech", "mech"), ("Civil", "civil"), ("IT", "IT")))
    class Meta:
        model = Seeker
        fields = ['looking_job_in','fname','lname']

class JobForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Job
        fields = '__all__'
