from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search by ideas',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a keyword...'})
    )
