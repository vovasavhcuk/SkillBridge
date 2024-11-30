from django.urls import path
from .views import ProposalListCreateAPIView, ProposalRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', ProposalListCreateAPIView.as_view(), name='proposal-list-create'),  # /api/proposals/
    path('<int:pk>/', ProposalRetrieveUpdateDeleteAPIView.as_view(), name='proposal-detail'),  # /api/proposals/<id>/
]