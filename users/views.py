# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': token.key,
            'full_name': user.get_full_name(),
            'short_name': user.get_short_name(),
            'email': user.email,
        }
        return Response(content)

class LogoutView(APIView):
    def get(self, request):
        content = {
            'status': 'Successfully Logged Out',
        }
        return Response(content)

class RegisterView(APIView):
    permission_classes = ()
    password = serializers.CharField(write_only=True)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            content = {
                'token': token.key,
                'full_name': user.get_full_name(),
                'short_name': user.get_short_name(),
                'email': user.email,
            }
            return Response(content)
        else:
            return Response(RegisterSerializer.errors, status=status.HTTP_400_BAD_REQUEST)