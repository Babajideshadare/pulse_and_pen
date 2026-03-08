from rest_framework.routers import DefaultRouter
from .api_views import BPEntryViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'bp-entries', BPEntryViewSet, basename='bp-entry')
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = router.urls