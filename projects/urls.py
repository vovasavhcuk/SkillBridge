from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteAPIView.as_view(), name='project-retrieve-update-delete'),
]
