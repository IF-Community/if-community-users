from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .api.serializers import AccountSerializer, ProfileSerializer
from accounts.models import Profile


# ========================= API V1 ======================================

class AccountViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )


    def partial_update(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        new_email = serializer.validated_data.get('email')
        existing_profiles = get_user_model().objects.exclude(pk=instance.pk).filter(email=new_email)
        if existing_profiles.exists():
            return Response({"error": f"Já existe um perfil com este e-mail!"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        return Response(serializer.data)

class ProfileViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )
