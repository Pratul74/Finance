from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    title=models.CharField(max_length=100, blank=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['title', 'user']

    def __str__(self):
        return self.title

class Record(models.Model):

    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='records'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='expense'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='records'
    )

    date = models.DateField()

    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Amount must be positive")
        
    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Type: {self.type}"
