from rest_framework import serializers
from .models import BPEntry, JournalEntry


class BPEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BPEntry
        fields = ['id', 'date', 'time', 'systolic', 'diastolic', 'pulse', 'note']

class JournalEntrySerializer(serializers.ModelSerializer):
    """
    Serialize JournalEntry for the API.
    """
    class Meta:
        model = JournalEntry
        fields = [
            'id',
            'date',
            'sleep_hours',
            'sleep_quality',
            'exercise_type',
            'exercise_duration',
            'diet_notes',
            'mood_stress_level',
        ]