from django.conf import settings
from django.db import models
from projects.models import Project

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="proposals")
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="proposals")
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='submitted'
    )

    def __str__(self):
        return f"{self.freelancer.username} - {self.project.title}"

