# core/enums.py

from django.db import models


class OrganisationType(models.TextChoices):
    REAL_ESTATE = "RealEstate"
    DISTRIBUTION = "Distribution"
    TRANSPORT = "Transport"
    INVESTMENT = "Investment"
    TRADING = "Trading"
    PROPERTY = "Property"
    OTHER = "Other"


class BranchType(models.TextChoices):
    MAIN = "Main"
    SUB = "Sub"
    AREA = "Area"


class DepoType(models.TextChoices):
    MAIN = "Main"
    SUB = "Sub"
    AREA = "Area"
    LOCALITY = "Locality"


class RoleType(models.TextChoices):
    ADMIN = "ADMIN"
    ACCOUNTS = "ACCOUNTS"
    HR = "HR"
    OPERATIONS = "OPERATIONS"
    TRANSPORT = "TRANSPORT"
    BROKER = "BROKER"
    ASSISTANT = "ASSISTANT"


class ModuleType(models.TextChoices):
    ADMIN = "Admin"
    HRMS = "HRMS"
    WEALTH = "Wealth"
    PURCHASE = "Purchase"
    SALES = "Sales"
    ASSETS = "Assets"


class SubModuleType(models.TextChoices):
    ORGANIZATION = "Organization"
    INVOICE = "Invoice"
    CONTRACTS = "Contracts"
    ORDERS_INDENTS = "Orders_Indents"
    REPORTS = "Reports"
