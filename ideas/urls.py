from django.urls import path
from ideas import views

urlpatterns = [
    path('add/', views.IdeaCreateView.as_view(), name='idea-create'),
    path('<int:pk>/edit/', views.IdeaUpdateView.as_view(), name='idea-edit'),
]