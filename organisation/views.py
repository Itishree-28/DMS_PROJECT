from rest_framework.viewsets import ModelViewSet
from .models import (
    OrgOwnerDetails, OrganisationDetail, OrgBusinessDetails,
    OrgBranchDetails, OrgDepoDetails
)
from .serializers import (
    OrgOwnerSerializer, OrganisationSerializer, OrgBusinessSerializer,
    OrgBranchSerializer, OrgDepoSerializer
)
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasModulePermission


class OrgOwnerViewSet(ModelViewSet):
    queryset = OrgOwnerDetails.objects.all()
    serializer_class = OrgOwnerSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Organization"


class OrganisationViewSet(ModelViewSet):
    queryset = OrganisationDetail.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Organization"

class OrgBusinessViewSet(ModelViewSet):
    queryset = OrgBusinessDetails.objects.all()
    serializer_class = OrgBusinessSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Organization"


class OrgBranchViewSet(ModelViewSet):
    queryset = OrgBranchDetails.objects.all()
    serializer_class = OrgBranchSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Organization"


class OrgDepoViewSet(ModelViewSet):
    queryset = OrgDepoDetails.objects.all()
    serializer_class = OrgDepoSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Organization"
