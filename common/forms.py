from django import forms

from common.models import Comment


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a keyword...'})
    )


class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ['text']
    widgets = {
        'text': forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Add a constructive comment...'}
        ),
    }
