from rest_framework import serializers
from .models import (
    VendorMaster,
    VendorAddress,
    VendorPlant,
    VendorBusinessDetails
)


class VendorAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAddress
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class VendorPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPlant
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class VendorBusinessDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBusinessDetails
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class VendorMasterSerializer(serializers.ModelSerializer):
    addresses = VendorAddressSerializer(many=True, read_only=True)
    plants = VendorPlantSerializer(many=True, read_only=True)
    business_details = VendorBusinessDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = VendorMaster
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
