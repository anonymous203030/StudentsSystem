from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8)

    class Meta:
        model= User
        fields = ('id', 'email', 'password',)
        ordering = ['-id']


    def validate(self, attrs):
        email=attrs.get('email', '')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', )
        ordering = ['-id']

    def validate(self,attrs):
        email=attrs.get('email', '')
        password =attrs.get('password','')

        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials,try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled')
        return {
            'email': user.email,
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password', 'is_student')
        extra_kwargs = {'password': { 'write_only':True,
                                      'min_length':8} }
        def create(self, validated_data):
            is_student = validated_data.pop('is_student')
            user = get_user_model().objects.create_user(**validated_data)
            user.is_student = is_student
            user.save()
            return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'preferred_name',
        'image', 'fb_profile', 'github_name', 'current_level',)
