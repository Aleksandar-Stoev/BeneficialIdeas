from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.forms import CustomUserCreationForm, ProfileEditForm, ProfileDeleteForm
from accounts.models import Profile

User = get_user_model()


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk=pk)

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    form_class = ProfileDeleteForm
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk=pk)

    def form_valid(self, form):
        profile = self.get_object()
        user = profile.user

        user.delete()

        return HttpResponseRedirect(self.get_success_url())
