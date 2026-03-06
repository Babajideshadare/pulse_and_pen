from rest_framework import serializers
from .models import BPEntry


class BPEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BPEntry
        fields = ['id', 'date', 'time', 'systolic', 'diastolic', 'pulse', 'note']