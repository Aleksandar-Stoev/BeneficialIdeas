from django import forms

from common.mixins import DisableFieldsMixin
from ideas.models import Idea


class IdeaBaseForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category', ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insert title here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your idea here'}),
        }
        error_messages = {
            'title': {
                'unique': 'The title of your idea should be unique, we already have an idea with this title',
            }
        }


class IdeaCreateForm(IdeaBaseForm):
    pass


class IdeaUpdateForm(IdeaBaseForm):
    pass


class IdeaDeleteForm(DisableFieldsMixin, IdeaBaseForm):
    pass
