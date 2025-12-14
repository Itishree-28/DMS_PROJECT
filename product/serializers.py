from rest_framework import serializers
from .models import (
    ProductMaster,
    InventoryMaster,
    PriceUpdateMaster
)

class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = "__all__"


class InventoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMaster
        fields = "__all__"


class PriceUpdateMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceUpdateMaster
        fields = "__all__"
