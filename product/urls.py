from rest_framework.routers import DefaultRouter
from .views import (
    ProductMasterViewSet,
    InventoryMasterViewSet,
    PriceUpdateMasterViewSet
)

router = DefaultRouter()

router.register("products", ProductMasterViewSet, basename="products")
router.register("inventory", InventoryMasterViewSet, basename="inventory")
router.register("price-update", PriceUpdateMasterViewSet, basename="price-update")

urlpatterns = router.urls
