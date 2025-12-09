from django.db import models
from core.models import BaseModel
from core.enums import RoleType, ModuleType, SubModuleType
from organisation.models import OrganisationDetail, OrgBranchDetails


class UserDetails(BaseModel):
    organisation = models.ForeignKey(OrganisationDetail, on_delete=models.CASCADE)
    branch = models.ForeignKey(OrgBranchDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

    class Meta:
        db_table = "user_details"

    def __str__(self):
        return self.username


class Role(BaseModel):
    type = models.CharField(max_length=50, choices=RoleType.choices)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.type


class UserRoles(BaseModel):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_roles"

class RoleAccess(BaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    module = models.CharField(max_length=50, choices=ModuleType.choices)
    submodule = models.CharField(max_length=50, choices=SubModuleType.choices)

    can_read = models.BooleanField(default=True)
    can_write = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "role_access"
        unique_together = ("role", "module", "submodule")

class UserAccess(BaseModel):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    module = models.CharField(max_length=50, choices=ModuleType.choices)
    submodule = models.CharField(max_length=50, choices=SubModuleType.choices)

    can_read = models.BooleanField(default=True)
    can_write = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    access_time = models.TimeField(null=True, blank=True)
    access_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "user_access"
        unique_together = ("user", "module", "submodule")

class UserTempAccess(BaseModel):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    module = models.CharField(max_length=50, choices=ModuleType.choices)
    submodule = models.CharField(max_length=50, choices=SubModuleType.choices)

    can_read = models.BooleanField(default=True)
    can_write = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    class Meta:
        db_table = "user_temp_access"
