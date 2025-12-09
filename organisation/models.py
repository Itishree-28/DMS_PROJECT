from django.db import models
from core.models import BaseModel
from core.enums import OrganisationType, BranchType, DepoType


class OrgOwnerDetails(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "org_owner_details"


class OrganisationDetail(BaseModel):
    registered_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    organisation_type = models.CharField(
        max_length=50, choices=OrganisationType.choices
    )
    owner = models.ForeignKey(OrgOwnerDetails, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "organisation_detail"


class OrgBusinessDetails(BaseModel):
    organisation = models.ForeignKey(
        OrganisationDetail, on_delete=models.CASCADE, related_name="business_info"
    )
    tin_no = models.CharField(max_length=255, null=True, blank=True)
    tin_date = models.DateField(null=True, blank=True)
    pan_no = models.CharField(max_length=255, null=True, blank=True)
    gstin = models.CharField(max_length=255, null=True, blank=True)
    et_no = models.CharField(max_length=255, null=True, blank=True)
    et_date = models.DateField(null=True, blank=True)
    cst_no = models.CharField(max_length=255, null=True, blank=True)
    cst_date = models.DateField(null=True, blank=True)
    trade_no = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "org_business_details"


class OrgBranchDetails(BaseModel):
    organisation = models.ForeignKey(
        OrganisationDetail, on_delete=models.CASCADE, related_name="branches"
    )
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    branch_head = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=BranchType.choices)

    class Meta:
        db_table = "org_branch_details"


class OrgDepoDetails(BaseModel):
    organisation = models.ForeignKey(
        OrganisationDetail, on_delete=models.CASCADE, related_name="depos"
    )
    branch = models.ForeignKey(
        OrgBranchDetails, on_delete=models.CASCADE, related_name="depos"
    )
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    series_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    depo_head = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=DepoType.choices)

    class Meta:
        db_table = "org_depo_details"
