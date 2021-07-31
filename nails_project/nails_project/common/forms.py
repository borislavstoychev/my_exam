from django import forms

from nails_project.common.models import Comment, Schedule


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'is_required': True,
                },
            ),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('date', 'time')
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'is_required': True,
                },
            ),
            'time': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'is_required': True,
                    'placeholder': 'Time',
                }
            )
        }



