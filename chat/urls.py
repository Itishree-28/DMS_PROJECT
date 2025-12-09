from rest_framework.routers import DefaultRouter
from .views import InternalChatViewSet

router = DefaultRouter()
router.register(r"chat", InternalChatViewSet, basename="chat")

urlpatterns = router.urls
