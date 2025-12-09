from rest_framework import serializers
from .models import (
    AssetMaster, AssetCategory, AssetAllocation,
    AssetMaintenance, AssetDepreciation, AssetDisposal
)

class AssetMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaster
        fields = "__all__"

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = "__all__"

class AssetAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAllocation
        fields = "__all__"

class AssetMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaintenance
        fields = "__all__"

class AssetDepreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDepreciation
        fields = "__all__"

class AssetDisposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDisposal
        fields = "__all__"
