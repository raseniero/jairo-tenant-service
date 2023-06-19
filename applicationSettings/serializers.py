from rest_framework import serializers
from .models import Application


class ApplicationSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = (
            "guid",
            "key",
            "value",

        )
