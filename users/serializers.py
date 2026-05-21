from rest_framework import serializers
from .models import User
from .services import create_user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'type',
        )
    def create(self, validated_data):
        return create_user(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'type',
        )