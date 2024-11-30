from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Proposal
from .serializers import ProposalSerializer

class ProposalListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Тільки залогінені користувачі

    def get(self, request):
        proposals = Proposal.objects.filter(freelancer=request.user)  # Фільтруємо лише для поточного користувача
        serializer = ProposalSerializer(proposals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(freelancer=request.user)  # Автоматично додаємо автора пропозиції
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProposalRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Тільки залогінені користувачі

    def get(self, request, pk):
        proposal = get_object_or_404(Proposal, pk=pk, freelancer=request.user)  # Перевіряємо, що це пропозиція користувача
        serializer = ProposalSerializer(proposal)
        return Response(serializer.data)

    def put(self, request, pk):
        proposal = get_object_or_404(Proposal, pk=pk, freelancer=request.user)
        serializer = ProposalSerializer(proposal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proposal = get_object_or_404(Proposal, pk=pk, freelancer=request.user)
        proposal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
