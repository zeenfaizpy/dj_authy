from rest_framework import serializers

from dj_authy.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "email"}
        }


class AuthyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = ["id", "email", "first_name", "last_name"]
