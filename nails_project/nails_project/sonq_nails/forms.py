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


class TypeFilterForm(forms.ModelForm):
    class Meta:
        model = Nails
        fields = ("type", )
    # MANICURE = 'M'
    # PEDICURE = 'P'
    # ALL = 'A'
    # CHOICES = [
    #         (ALL, 'All'),
    #         (MANICURE, 'Manicure'),
    #         (PEDICURE, 'Pedicure'),
    #         (PEDICURE, 'Else'),
    #     ]
    # type = forms.ChoiceField(
    #     required=False,
    #     choices=CHOICES,
    #     widget=forms.Select(attrs={'style': 'width:10%; font-size: 20px; text-align: center;', 'class': 'form-select'})
    # )
