from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.permissions import HasModulePermission

from .models import (
    VendorMaster,
    VendorAddress,
    VendorPlant,
    VendorBusinessDetails,
)

from .serializers import (
    VendorMasterSerializer,
    VendorAddressSerializer,
    VendorPlantSerializer,
    VendorBusinessDetailsSerializer,
)


class VendorMasterViewSet(ModelViewSet):
    queryset = VendorMaster.objects.all()
    serializer_class = VendorMasterSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Vendor"
    submodule = "Master"


class VendorAddressViewSet(ModelViewSet):
    queryset = VendorAddress.objects.all()
    serializer_class = VendorAddressSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Vendor"
    submodule = "Address"


class VendorPlantViewSet(ModelViewSet):
    queryset = VendorPlant.objects.all()
    serializer_class = VendorPlantSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Vendor"
    submodule = "Plant"


class VendorBusinessDetailsViewSet(ModelViewSet):
    queryset = VendorBusinessDetails.objects.all()
    serializer_class = VendorBusinessDetailsSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Vendor"
    submodule = "BusinessDetails"
