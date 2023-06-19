from rest_framework import serializers
from .models import Software


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = (
            "guid",            
            "name",
            "description",
            "applicationCategory",
            "applicationSubCategory",
            "applicationSuite",
            "softwareVersion",

        )
