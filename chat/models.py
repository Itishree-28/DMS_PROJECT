from django.db import models
from core.models import BaseModel
from users.models import UserDetails


class InternalChat(BaseModel):
    sender = models.ForeignKey(
        UserDetails,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        UserDetails,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )
    message = models.TextField(null=True, blank=True)
    attachment_path = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

    class Meta:
        db_table = "internal_chat"
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.sender.name} → {self.receiver.name}"
