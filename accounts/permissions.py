from rest_framework.permissions import BasePermission
from rest_framework_api_key.permissions import HasAPIKey

class IsAuthenticatedOrHasApiKey(BasePermission):
    def has_permission(self, request, view):
        return HasAPIKey().has_permission(request, view) or request.user and request.user.is_authenticated
