from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrgOwnerViewSet,
    OrganisationViewSet,
    OrgBusinessViewSet,
    OrgBranchViewSet,
    OrgDepoViewSet
)

router = DefaultRouter()
router.register(r"owner", OrgOwnerViewSet)
router.register(r"organisation", OrganisationViewSet)
router.register(r"business", OrgBusinessViewSet)
router.register(r"branch", OrgBranchViewSet)
router.register(r"depo", OrgDepoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
