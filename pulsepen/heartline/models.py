from django.db import models
from django.contrib.auth.models import User


class BPEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time} ({self.systolic}/{self.diastolic})"


class JournalEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )
    date = models.DateField()
    sleep_hours = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        help_text="Hours of sleep, e.g. 7.5"
    )
    sleep_quality = models.CharField(
        max_length=50,
        blank=True,
        help_text="Short description or rating of sleep quality"
    )
    exercise_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Type of exercise, e.g. walking, running"
    )
    exercise_duration = models.IntegerField(
        blank=True,
        null=True,
        help_text="Duration of exercise in minutes"
    )
    diet_notes = models.TextField(
        blank=True,
        help_text="Notes about meals or diet for the day"
    )
    mood_stress_level = models.CharField(
        max_length=50,
        blank=True,
        help_text="Mood/stress description, e.g. 'calm', 'stressed'"
    )

    def __str__(self):
        return f"{self.user.username} - {self.date} journal entry"