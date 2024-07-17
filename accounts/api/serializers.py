from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounts.models import Profile, Report

class AccountSerializer(ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'profile_name', 'profile_bio', 'profile_photo', 'profile_background', 'user']

class ReportSerializer(ModelSerializer):

    class Meta:
        model = Report
        fields = ['id', 'reported_by', 'reported_user', 'category', 'description', 'created_at']