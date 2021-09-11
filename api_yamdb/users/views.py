import json
from random import choice

from rest_framework.views import APIView
from rest_framework import generics, serializers, status, viewsets
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import filters, mixins, permissions, viewsets

from .models import User
from .serializers import GetTokenSerializer, SignupSerializer
from .utils import Util

class CreateModelViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class SignupViewSet(CreateModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class APIGetToken(APIView):
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = User.objects.get(username=data['username'])
        if data.get('confirmation_code') == user.confirmation_code:
            token = RefreshToken.for_user(user).access_token
            return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
