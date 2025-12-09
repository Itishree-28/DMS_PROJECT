from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasModulePermission

from .models import (
    AssetMaster, AssetCategory, AssetAllocation,
    AssetMaintenance, AssetDepreciation, AssetDisposal
)
from .serializers import (
    AssetMasterSerializer, AssetCategorySerializer, AssetAllocationSerializer,
    AssetMaintenanceSerializer, AssetDepreciationSerializer, AssetDisposalSerializer
)


class AssetMasterViewSet(ModelViewSet):
    queryset = AssetMaster.objects.all()
    serializer_class = AssetMasterSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Master"


class AssetCategoryViewSet(ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Category"


class AssetAllocationViewSet(ModelViewSet):
    queryset = AssetAllocation.objects.all()
    serializer_class = AssetAllocationSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Allocation"


class AssetMaintenanceViewSet(ModelViewSet):
    queryset = AssetMaintenance.objects.all()
    serializer_class = AssetMaintenanceSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Maintenance"


class AssetDepreciationViewSet(ModelViewSet):
    queryset = AssetDepreciation.objects.all()
    serializer_class = AssetDepreciationSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Depreciation"


class AssetDisposalViewSet(ModelViewSet):
    queryset = AssetDisposal.objects.all()
    serializer_class = AssetDisposalSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Assets"
    submodule = "Disposal"
