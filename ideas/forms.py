from django import forms
from django.forms import inlineformset_factory
from supplies.models import Supplies
from ideas.models import Idea


class IdeaForm(forms.ModelForm):  # TODO: make a base form
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category', ]


SuppliesFormSet = inlineformset_factory(
    Idea,
    Supplies,
    fields=['name', 'quantity', 'is_secured'],
    extra=3,
    can_delete=True
)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Търсене',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a keyword...'})
    )
