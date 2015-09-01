from rest_framework import serializers
from oauth2_provider.models import Application
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    client_id = serializers.SerializerMethodField()
    client_secret = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'client_id', 'client_secret')
        write_only_fields = ('password',)

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    def get_client_id(self, obj):
        return Application.objects.get(user=obj).client_id

    def get_client_secret(self, obj):
        return Application.objects.get(user=obj).client_secret


class LoginSerializer(SignUpSerializer):
    class Meta:
        model = User
        fields = ('client_id', 'client_secret')

