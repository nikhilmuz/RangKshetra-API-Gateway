import re
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)

        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg)
        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta():
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')