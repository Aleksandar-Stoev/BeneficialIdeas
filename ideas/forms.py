from django import forms
from django.forms import inlineformset_factory
from supplies.models import Supplies
from ideas.models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category', ]


SuppliesFormSet = inlineformset_factory(  # TODO: make it optional
    Idea,
    Supplies,
    fields=['name', 'quantity', 'is_secured'],  # TODO: remove 'is_secured'
    extra=3,
    can_delete=True
)
