from django.db import models
from core.models import BaseModel
from core.enums import TransactionType, TransactionStatus


class VendorMaster(BaseModel):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "vendor_master"
        ordering = ["name"]

    def __str__(self):
        return self.name


class VendorAddress(BaseModel):
    vendor = models.ForeignKey(
        VendorMaster,
        on_delete=models.CASCADE,
        related_name="addresses"
    )
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=20)

    class Meta:
        db_table = "vendor_address"
        ordering = ["city"]

    def __str__(self):
        return f"{self.address_line1}, {self.city}"


class VendorPlant(BaseModel):
    vendor = models.ForeignKey(
        VendorMaster,
        on_delete=models.CASCADE,
        related_name="plants"
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    pin = models.CharField(max_length=20)

    class Meta:
        db_table = "vendor_plant"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.city})"


class VendorBusinessDetails(BaseModel):
    vendor = models.ForeignKey(
        VendorMaster,
        on_delete=models.CASCADE,
        related_name="business_details"
    )
    transaction_type = models.CharField(max_length=20, choices=TransactionType.choices)
    transaction_status = models.CharField(max_length=20, choices=TransactionStatus.choices)
    
    igst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True)
    gstin = models.CharField(max_length=255, blank=True, null=True)

    tin_no = models.CharField(max_length=255, blank=True, null=True)
    tin_date = models.DateField(blank=True, null=True)

    cst_no = models.CharField(max_length=255, blank=True, null=True)
    cst_date = models.DateField(blank=True, null=True)

    et_no = models.CharField(max_length=255, blank=True, null=True)
    et_date = models.DateField(blank=True, null=True)

    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "vendor_business_details"
        ordering = ["vendor"]

    def __str__(self):
        return f"{self.vendor.name} - {self.transaction_type}"
