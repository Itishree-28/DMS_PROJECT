from django.db import models
from core.models import BaseModel
from users.models import UserDetails


class DocumentManagement(BaseModel):
    user = models.ForeignKey(
        UserDetails,
        on_delete=models.CASCADE,
        related_name="documents"
    )
    document_type = models.CharField(max_length=255)
    document_name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to="documents/")
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "document_management"
        ordering = ["-uploaded_on"]

    def __str__(self):
        return f"{self.document_name} ({self.document_type})"
