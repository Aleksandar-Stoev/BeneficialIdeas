from django import forms
from django.core.exceptions import ValidationError
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
                'required': 'Every great idea needs a name — please enter a title.',
                'max_length': 'Your title is a bit too long. Please keep it short and punchy (under 150 characters).',
            },
            'description': {
                'required': 'Please provide a description so others can understand your idea.',
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            qs = Idea.objects.filter(title__iexact=title)

            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise ValidationError(
                    self.Meta.error_messages['title']['unique'],
                    code='unique',
                )
        return title


class IdeaCreateForm(IdeaBaseForm):
    pass


class IdeaUpdateForm(IdeaBaseForm):
    pass


class IdeaDeleteForm(DisableFieldsMixin, IdeaBaseForm):
    pass
