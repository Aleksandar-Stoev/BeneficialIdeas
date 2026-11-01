from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Търсене',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a keyword...'})
    )
