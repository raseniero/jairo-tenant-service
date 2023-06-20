from rest_framework import serializers
from .models import ApplicationSettings


class ApplicationSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationSettings
        fields = (
            "guid",
            "key",
            "value",

        )
