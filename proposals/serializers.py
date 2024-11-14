from rest_framework import serializers
from .models import Proposal

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'project', 'freelancer', 'bid_amount', 'cover_letter', 'submitted_at', 'status']
