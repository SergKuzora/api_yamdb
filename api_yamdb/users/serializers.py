from rest_framework import serializers
from . models import User


class SignupSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('email', 'username')


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
