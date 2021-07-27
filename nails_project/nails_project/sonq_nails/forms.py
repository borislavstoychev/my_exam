from django import forms

from nails_project.sonq_nails.models import Nails


class NailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            if _ == "type":
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Nails
        exclude = ('user', 'is_complete')
