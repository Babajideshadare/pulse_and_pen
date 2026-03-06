from rest_framework.routers import DefaultRouter
from .api_views import BPEntryViewSet

router = DefaultRouter()
router.register(r'bp-entries', BPEntryViewSet, basename='bp-entry')

urlpatterns = router.urls