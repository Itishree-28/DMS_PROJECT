from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import UserDetails


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = UserDetails.objects.get(username=username)
        except UserDetails.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password.")

        if not check_password(password, user.password_hash):
            raise serializers.ValidationError("Invalid username or password.")

        data["user"] = user
        return data
