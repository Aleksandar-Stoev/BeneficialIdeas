from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='details'),
        path('edit/', views.ProfileUpdateView.as_view(), name='edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete'),
    ])),
]
