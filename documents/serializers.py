from rest_framework import serializers
from .models import DocumentManagement


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentManagement
        fields = "__all__"
        read_only_fields = ["uploaded_on"]
