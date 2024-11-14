from django.db import models
from proposals.models import Proposal

class Payment(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')],
        default='pending'
    )

    def __str__(self):
        return f"Payment for {self.proposal.project.title} - {self.amount}"
