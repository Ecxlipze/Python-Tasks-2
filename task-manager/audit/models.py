from django.contrib.auth.models import User
from django.db import models

class AuditLog(models.Model):
    ACTIONS = [
        ("CREATE", "Create"),
        ("UPDATE", "Update"),
        ("DELETE", "Delete"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    action = models.CharField(
        max_length=10,
        choices=ACTIONS,
    )
    object_type = models.CharField(
        max_length=100,
    )
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    def __str__(self):
        return f"{self.user.username} - {self.action}"