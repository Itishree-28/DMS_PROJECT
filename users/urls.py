from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserDetailsViewSet,
    RoleViewSet,
    UserRolesViewSet,
    UserAccessViewSet,
    UserTempAccessViewSet,
    RoleAccessViewSet,
    login_view
)

router = DefaultRouter()
router.register(r"users", UserDetailsViewSet, basename="users")
router.register(r"roles", RoleViewSet, basename="roles")
router.register("role-access", RoleAccessViewSet)
router.register(r"user-roles", UserRolesViewSet, basename="user-roles")
router.register(r"access", UserAccessViewSet, basename="access")
router.register(r"temp-access", UserTempAccessViewSet, basename="temp-access")

urlpatterns = [
    path("login/", login_view, name="login"),   # ✅ JWT Login API
    path("", include(router.urls)),             # CRUD routes for all viewsets
]
