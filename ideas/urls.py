from django.urls import path, include
from ideas import views

app_name = 'ideas'

urlpatterns = [
    path('', views.IdeaListView.as_view(), name='list'),
    path('add/', views.IdeaCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', views.IdeaDetailView.as_view(), name='detail'),
        path('edit/', views.IdeaUpdateView.as_view(), name='edit'),
        path('support/', views.support_idea_view, name='support'),
    ]))
]
