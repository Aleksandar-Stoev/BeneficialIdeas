from django.urls import path
from common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
]
