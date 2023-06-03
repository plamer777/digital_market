"""This file contains serializers to work with User models"""
from rest_framework import serializers
from core.models import User
# -------------------------------------------------------------------------


class UserCreateSerializer(serializers.ModelSerializer):
    """This serializer is used to create a new user"""
    password_repeat = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_repeat']

    def validate(self, attrs: dict) -> dict:
        """This method allows to validate passwords during registration"""
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')

        if password and password == password_repeat:
            attrs.pop('password_repeat', None)
            self.fields.pop('password_repeat', None)
            return super().validate(attrs)

        raise serializers.ValidationError('The passwords do not match')
