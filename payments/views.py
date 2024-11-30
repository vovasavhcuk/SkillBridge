from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(client=request.user)  # Фільтруємо за клієнтом
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['client'] = request.user.id  # Додаємо поле 'client'
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Тільки залогінені користувачі

    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, client=request.user)  # Перевіряємо, що це платіж користувача
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, client=request.user)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, client=request.user)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
