from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_image']


class ProfileDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        label="I confirm that I want the account to be permanently deleted.",
        required=True
    )


class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'] = forms.EmailField(
            label='Email address',
            widget=forms.EmailInput(attrs={'autofocus': True, 'autocomplete': 'email'})
        )
        self.fields['password'].label = 'Password'
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'autocomplete': 'current-password'}
        )
