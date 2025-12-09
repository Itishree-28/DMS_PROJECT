from django.db import models
from core.models import BaseModel
from users.models import UserDetails
# from vendor.models import VendorMaster
# from purchase.models import PurchaseInvoice


class AssetCategory(BaseModel):
    DEPRECIATION_METHOD = (
        ("StraightLine", "Straight Line"),
        ("ReducingBalance", "Reducing Balance"),
        ("Other", "Other"),
    )

    category_name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    useful_life = models.IntegerField(null=True, blank=True)

    default_depreciation_method = models.CharField(
        max_length=50, choices=DEPRECIATION_METHOD
    )
    default_depreciation_rate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    class Meta:
        db_table = "asset_category"

    def __str__(self):
        return self.category_name


class AssetMaster(BaseModel):
    class Category(models.TextChoices):
        IT = "IT", "IT"
        FURNITURE = "Furniture", "Furniture"
        MACHINERY = "Machinery", "Machinery"
        ELECTRONICS = "Electronics", "Electronics"
        OTHER = "Other", "Other"

    class AssetType(models.TextChoices):
        MOVABLE = "Movable", "Movable"
        FIXED = "Fixed", "Fixed"

    class DepreciationMethod(models.TextChoices):
        SL = "StraightLine", "Straight Line"
        RB = "ReducingBalance", "Reducing Balance"
        OTHER = "Other", "Other"

    asset_name = models.CharField(max_length=255)
    asset_code = models.CharField(max_length=255)

    category = models.CharField(max_length=50, choices=Category.choices)
    asset_type = models.CharField(max_length=20, choices=AssetType.choices)

    serial_number = models.CharField(max_length=255, null=True, blank=True)
    model_number = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)

    purchase_date = models.DateField(null=True, blank=True)
    # purchase_vendor = models.ForeignKey(
    #     VendorMaster, on_delete=models.SET_NULL, null=True, blank=True
    # )
    # purchase_invoice = models.ForeignKey(
    #     PurchaseInvoice, on_delete=models.SET_NULL, null=True, blank=True
    # )

    cost_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    depreciation_method = models.CharField(
        max_length=50, choices=DepreciationMethod.choices
    )
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    warranty_expiry_date = models.DateField(null=True, blank=True)
    insurance_policy = models.CharField(max_length=255, null=True, blank=True)
    insurance_expiry_date = models.DateField(null=True, blank=True)

    barcode_number = models.CharField(max_length=255, null=True, blank=True)
    location_description = models.CharField(max_length=255, null=True, blank=True)

    assigned_to = models.ForeignKey(
        UserDetails, on_delete=models.SET_NULL, null=True, blank=True
    )

    status = models.CharField(max_length=50, default="Active")

    class Meta:
        db_table = "asset_master"

    def __str__(self):
        return f"{self.asset_name} ({self.asset_code})"


class AssetAllocation(BaseModel):
    asset = models.ForeignKey(
        AssetMaster, on_delete=models.CASCADE, related_name="allocations"
    )

    assigned_to = models.ForeignKey(
        UserDetails, on_delete=models.SET_NULL, null=True, blank=True
    )

    allocation_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    condition_at_issue = models.CharField(max_length=255, null=True, blank=True)
    condition_at_return = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "asset_allocation"

    def __str__(self):
        return f"Allocation {self.id}"


class AssetMaintenance(BaseModel):
    asset = models.ForeignKey(
        AssetMaster, on_delete=models.CASCADE, related_name="maintenance_records"
    )

    service_type = models.CharField(max_length=255)
    service_provider = models.CharField(max_length=255, null=True, blank=True)
    service_date = models.DateField()
    next_service_due_date = models.DateField(null=True, blank=True)

    cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=255, default="Pending")

    file_path = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "asset_maintenance"


class AssetDepreciation(BaseModel):
    class DepMethod(models.TextChoices):
        SL = "StraightLine", "Straight Line"
        RB = "ReducingBalance", "Reducing Balance"
        OTHER = "Other", "Other"

    asset = models.ForeignKey(
        AssetMaster, on_delete=models.CASCADE, related_name="depreciation_records"
    )

    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2)
    depreciation_method = models.CharField(max_length=50, choices=DepMethod.choices)

    depreciation_start_date = models.DateField()
    current_value = models.DecimalField(max_digits=12, decimal_places=2)

    fiscal_year = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Active")

    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "asset_depreciation"


class AssetDisposal(BaseModel):
    asset = models.ForeignKey(AssetMaster, on_delete=models.CASCADE)

    disposal_type = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=255)
    sale_value = models.DecimalField(max_digits=12, decimal_places=2)
    disposal_date = models.DateField()

    approval_document_path = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "asset_disposal"

    def __str__(self):
        return f"{self.asset.asset_name} - Disposal"
