from django import forms

from expenses_tracker2.profiles.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

