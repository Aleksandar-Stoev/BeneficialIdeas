from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]
