from datetime import datetime
from rest_framework.permissions import BasePermission
from .models import UserAccess, UserTempAccess, RoleAccess, UserRoles


class HasModulePermission(BasePermission):
    """
    Custom permission class for ERP Module + SubModule access.
    Checks in this priority:

        1. UserTempAccess  (highest)
        2. UserAccess      (override)
        3. RoleAccess      (default permissions)

    For each check, verifies:
        - can_read   (GET, HEAD)
        - can_write  (POST, PUT, PATCH)
        - can_delete (DELETE)
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        module = getattr(view, "module", None)
        submodule = getattr(view, "submodule", None)

        # If a ViewSet does NOT define module/submodule, allow access
        if module is None or submodule is None:
            return True

        # Determine requested permission type
        required_perm = self.get_required_permission(request)

        # 1️⃣ Check TEMPORARY ACCESS first
        temp_access = self.get_temp_access(user, module, submodule)
        if temp_access:
            return getattr(temp_access, required_perm, False)

        # 2️⃣ Check USER ACCESS override
        user_access = self.get_user_access(user, module, submodule)
        if user_access:
            return getattr(user_access, required_perm, False)

        # 3️⃣ Check ROLE ACCESS
        role_access = self.get_role_access(user, module, submodule)
        if role_access:
            return getattr(role_access, required_perm, False)

        return False  # Default deny

    # Helper: Determine required permission
    def get_required_permission(self, request):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return "can_read"
        elif request.method in ("POST", "PUT", "PATCH"):
            return "can_write"
        elif request.method == "DELETE":
            return "can_delete"
        return "can_read"

    # Helper: UserTempAccess (highest priority)
    def get_temp_access(self, user, module, submodule):
        now = datetime.now()
        return UserTempAccess.objects.filter(
            user=user,
            module=module,
            submodule=submodule,
            valid_from__lte=now,
            valid_to__gte=now
        ).first()

    # Helper: UserAccess (override)
    def get_user_access(self, user, module, submodule):
        return UserAccess.objects.filter(
            user=user,
            module=module,
            submodule=submodule
        ).first()

    # Helper: RoleAccess (default)
    def get_role_access(self, user, module, submodule):
        user_roles = UserRoles.objects.filter(user=user).values_list("role_id", flat=True)
        return RoleAccess.objects.filter(
            role_id__in=user_roles,
            module=module,
            submodule=submodule
        ).first()
