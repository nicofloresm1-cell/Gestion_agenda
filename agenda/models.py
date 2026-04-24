from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({'✓' if self.completed else 'Pendiente'})"