from django.urls import path
from .views import PaymentListCreateAPIView, PaymentRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('<int:pk>/', PaymentRetrieveUpdateDeleteAPIView.as_view(), name='payment-retrieve-update-delete'),
]