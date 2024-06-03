from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """
    This permission checks whether the user is a staff or owner of the object itself.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
    

