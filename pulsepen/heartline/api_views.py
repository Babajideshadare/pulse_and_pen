from rest_framework import viewsets, permissions
from .models import BPEntry
from .api_serializers import BPEntrySerializer


class BPEntryViewSet(viewsets.ModelViewSet):
    serializer_class = BPEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user).order_by('-date', '-time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
