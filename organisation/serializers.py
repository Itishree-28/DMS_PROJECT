from rest_framework import serializers
from .models import (
    OrgOwnerDetails, OrganisationDetail, OrgBusinessDetails,
    OrgBranchDetails, OrgDepoDetails
)


class OrgOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgOwnerDetails
        fields = "__all__"


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationDetail
        fields = "__all__"


class OrgBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgBusinessDetails
        fields = "__all__"


class OrgBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgBranchDetails
        fields = "__all__"


class OrgDepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgDepoDetails
        fields = "__all__"
