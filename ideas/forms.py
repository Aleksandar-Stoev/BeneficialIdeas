from django import forms
from ideas.models import Idea


class IdeaForm(forms.ModelForm):  # TODO: make a base form
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category', ]
