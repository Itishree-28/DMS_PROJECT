from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    VendorMasterViewSet,
    VendorAddressViewSet,
    VendorPlantViewSet,
    VendorBusinessDetailsViewSet,
)

router = DefaultRouter()
router.register("vendors", VendorMasterViewSet, basename="vendors")
router.register("vendor-address", VendorAddressViewSet, basename="vendor-address")
router.register("vendor-plant", VendorPlantViewSet, basename="vendor-plant")
router.register("vendor-business", VendorBusinessDetailsViewSet, basename="vendor-business")

urlpatterns = [
    path("", include(router.urls)),
]
