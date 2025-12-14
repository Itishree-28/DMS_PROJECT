from django.db import models
from core.models import BaseModel
from vendor.models import VendorMaster
from product.models import ProductMaster
from users.models import UserDetails


#  PRODUCT MASTER

class ProductMaster(BaseModel):
    product_id = models.UUIDField(primary_key=True, editable=False)

    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)

    u_unit = models.CharField(max_length=255)
    l_unit = models.CharField(max_length=255)

    case_quantity = models.IntegerField()
    packaging_type = models.CharField(max_length=255)

    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)

    excise_tax = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=10, decimal_places=2)
    cst_percent = models.DecimalField(max_digits=10, decimal_places=2)

    opening_balance = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.DecimalField(max_digits=10, decimal_places=2)

    hsn_code = models.CharField(max_length=255)
    broker_percent = models.DecimalField(max_digits=10, decimal_places=2)
    broker_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "product_master"

    def __str__(self):
        return self.name



#  INVENTORY MASTER

class InventoryMaster(BaseModel):
    inventory_id = models.UUIDField(primary_key=True, editable=False)

    vendor = models.ForeignKey(
        VendorMaster,
        on_delete=models.CASCADE,
        db_column="vendor_id"
    )

    product = models.ForeignKey(
        ProductMaster,
        on_delete=models.CASCADE,
        db_column="product_id"
    )

    product_group_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    hsn_code = models.CharField(max_length=255)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)

    case_quantity = models.IntegerField()
    total_stock_available = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_stock_balance = models.DecimalField(max_digits=10, decimal_places=2)

    last_updated = models.DateTimeField()

    class Meta:
        db_table = "inventory_master"

    def __str__(self):
        return f"{self.product.name} - {self.total_stock_available}"



#  PRICE UPDATE MASTER

class PriceUpdateMaster(BaseModel):
    price_update_id = models.UUIDField(primary_key=True, editable=False)

    vendor = models.ForeignKey(
        VendorMaster,
        on_delete=models.CASCADE,
        db_column="vendor_id"
    )

    product = models.ForeignKey(
        ProductMaster,
        on_delete=models.CASCADE,
        db_column="product_id"
    )

    product_group_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    hsn_code = models.CharField(max_length=255)

    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

    created_by = models.ForeignKey(
        UserDetails,
        on_delete=models.SET_NULL,
        null=True,
        db_column="created_by"
    )

    class Meta:
        db_table = "price_update_master"

    def __str__(self):
        return f"{self.product.name} - New MRP: {self.mrp}"
