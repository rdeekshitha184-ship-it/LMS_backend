from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'subject', 'title', 'description', 'file', 'uploaded_by', 'created_at']