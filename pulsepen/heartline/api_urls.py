from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import BPEntryViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'bp-entries', BPEntryViewSet, basename='bp-entry')
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = [
    path('token/', obtain_auth_token, name='api-token'),
] + router.urls