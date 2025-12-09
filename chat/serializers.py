from rest_framework import serializers
from .models import InternalChat


class InternalChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalChat
        fields = "__all__"
        read_only_fields = ["timestamp", "read_status"]
