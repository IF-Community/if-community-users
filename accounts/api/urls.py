from rest_framework import routers

from accounts.api.viewsets import AccountViewSet, ProfileViewSet

router = routers.SimpleRouter()

router.register(r'accounts', AccountViewSet, basename="accounts")
router.register(r'profiles', ProfileViewSet, basename="profiles")