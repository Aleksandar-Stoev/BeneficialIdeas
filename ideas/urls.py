from django.urls import path
from ideas import views

urlpatterns = [
    path('', views.IdeaListView.as_view(), name='idea-list'),
    path('<int:pk>/', views.IdeaDetailView.as_view(), name='idea-detail'),
    path('add/', views.IdeaCreateView.as_view(), name='idea-create'),
    path('<int:pk>/edit/', views.IdeaUpdateView.as_view(), name='idea-edit'),
    path('idea/<int:pk>/support/', views.support_idea_view, name='support-idea'),
]
