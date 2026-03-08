from rest_framework import viewsets, permissions
from .models import BPEntry, JournalEntry
from .api_serializers import BPEntrySerializer, JournalEntrySerializer


class BPEntryViewSet(viewsets.ModelViewSet):
    serializer_class = BPEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user).order_by('-date', '-time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on JournalEntry, per user.
    """
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)