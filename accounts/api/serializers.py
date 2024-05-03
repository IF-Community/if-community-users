from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from accounts.models import Profile

class AccountSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'profile_name', 'profile_bio', 'profile_photo', 'profile_background', 'user']
