from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[('admin', 'Admin'),
          ('viewer', 'Viewer'),
          ('analyst', 'Analyst')]
    USERNAME_FIELD='email'
    username=None
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email



