from django import forms

from nails_project.common.models import Comment


class CommentForm(forms.Form):

    comment = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Comment
        fields = ('comment',)


