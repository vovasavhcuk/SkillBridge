from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = [
        ('client', 'Client'),
        ('freelancer', 'Freelancer')
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)  # for freelancers
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
