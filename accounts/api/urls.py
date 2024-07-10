from rest_framework import routers

from accounts.api.viewsets import AccountViewSet, ProfileViewSet, ReportViewSet

router = routers.SimpleRouter()

router.register(r'accounts', AccountViewSet, basename="accounts")
router.register(r'profiles', ProfileViewSet, basename="profiles")
router.register(r'reports', ReportViewSet, basename="reports")