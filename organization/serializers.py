from rest_framework import serializers
from .models import Organization


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "url",
            "id",
            "name",
            "description",
            "subdomain",
            "created_at",
            "updated_at",
            "telephone",
            "tax_id",
            "logo",
            "address",
            "legal_name",
            "fax_number",
            "dun_number",
            "website",
        )
