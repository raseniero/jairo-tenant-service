from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(
        view_name="user-detail", format="html"
    )

    class Meta:
        model = User
        fields = (
            "url",
            "id",
            "highlight",
            "username",
            "password",
            "email",
            "phone",
        )
