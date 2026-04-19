from rest_framework import serializers
from .models import TimetableEntry

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableEntry
        fields = ['id', 'day', 'period', 'subject', 'teacher_name', 'start_time', 'end_time']