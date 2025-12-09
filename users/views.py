from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, action
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import HasModulePermission
from .models import (
    UserDetails, Role, UserRoles,
    UserAccess, UserTempAccess, RoleAccess
)
from .serializers import (
    UserDetailsSerializer, RoleSerializer, UserRolesSerializer,
    UserAccessSerializer, UserTempAccessSerializer, RoleAccessSerializer
)
from .serializers_auth import LoginSerializer

@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data["user"]
    refresh = RefreshToken.for_user(user)

    return Response({
        "message": "Login successful",
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user_id": str(user.id),
        "username": user.username
    })

class UserDetailsViewSet(ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "UserManagement"

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "Roles"

class UserRolesViewSet(ModelViewSet):
    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "Roles"

class RoleAccessViewSet(ModelViewSet):
    queryset = RoleAccess.objects.all()
    serializer_class = RoleAccessSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "RoleAccess"

    @action(detail=False, methods=["GET"], url_path="role/(?P<role_id>[^/.]+)")
    def get_role_permissions(self, request, role_id=None):
        data = RoleAccess.objects.filter(role_id=role_id)
        return Response(RoleAccessSerializer(data, many=True).data)

class UserAccessViewSet(ModelViewSet):
    queryset = UserAccess.objects.all()
    serializer_class = UserAccessSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "UserAccess"

    @action(detail=False, methods=["GET"], url_path="user/(?P<user_id>[^/.]+)")
    def get_user_permissions(self, request, user_id=None):
        data = UserAccess.objects.filter(user_id=user_id)
        return Response(UserAccessSerializer(data, many=True).data)

class UserTempAccessViewSet(ModelViewSet):
    queryset = UserTempAccess.objects.all()
    serializer_class = UserTempAccessSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module = "Admin"
    submodule = "TempAccess"

    @action(detail=False, methods=["GET"], url_path="user/(?P<user_id>[^/.]+)")
    def get_user_temp_access(self, request, user_id=None):
        data = UserTempAccess.objects.filter(user_id=user_id)
        return Response(UserTempAccessSerializer(data, many=True).data)
