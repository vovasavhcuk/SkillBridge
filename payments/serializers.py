from rest_framework import serializers

from proposals.models import Proposal
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'proposal', 'amount', 'payment_date', 'status']

proposal = serializers.PrimaryKeyRelatedField(queryset=Proposal.objects.all())
