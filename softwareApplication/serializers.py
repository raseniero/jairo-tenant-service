from rest_framework import serializers
from .models import SoftwareApplication


class SoftwareApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftwareApplication
        fields = (
            "guid",            
            "name",
            "description",
            "applicationCategory",
            "applicationSubCategory",
            "applicationSuite",
            "softwareVersion",

        )
