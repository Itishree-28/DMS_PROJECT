from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AssetMasterViewSet, AssetCategoryViewSet, AssetAllocationViewSet,
    AssetMaintenanceViewSet, AssetDepreciationViewSet, AssetDisposalViewSet
)

router = DefaultRouter()
router.register("master", AssetMasterViewSet)
router.register("category", AssetCategoryViewSet)
router.register("allocation", AssetAllocationViewSet)
router.register("maintenance", AssetMaintenanceViewSet)
router.register("depreciation", AssetDepreciationViewSet)
router.register("disposal", AssetDisposalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
