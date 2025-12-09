from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    UserDetails, Role, UserRoles,
    UserAccess, UserTempAccess, RoleAccess
)


class UserDetailsSerializer(serializers.ModelSerializer):
    password_hash = serializers.CharField(write_only=True)

    class Meta:
        model = UserDetails
        fields = "__all__"

    def create(self, validated_data):
        pwd = validated_data.pop("password_hash")
        validated_data["password_hash"] = make_password(pwd)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password_hash" in validated_data:
            validated_data["password_hash"] = make_password(validated_data["password_hash"])
        return super().update(instance, validated_data)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RoleAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAccess
        fields = "__all__"


class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = "__all__"


class UserAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccess
        fields = "__all__"


class UserTempAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTempAccess
        fields = "__all__"
