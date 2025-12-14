from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasModulePermission

from .models import (
    ProductMaster,
    InventoryMaster,
    PriceUpdateMaster
)

from .serializers import (
    ProductMasterSerializer,
    InventoryMasterSerializer,
    PriceUpdateMasterSerializer
)


class ProductMasterViewSet(ModelViewSet):
    queryset = ProductMaster.objects.all()
    serializer_class = ProductMasterSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Inventory"
    submodule = "ProductMaster"


class InventoryMasterViewSet(ModelViewSet):
    queryset = InventoryMaster.objects.all()
    serializer_class = InventoryMasterSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Inventory"
    submodule = "InventoryMaster"


class PriceUpdateMasterViewSet(ModelViewSet):
    queryset = PriceUpdateMaster.objects.all()
    serializer_class = PriceUpdateMasterSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Inventory"
    submodule = "PriceUpdate"
