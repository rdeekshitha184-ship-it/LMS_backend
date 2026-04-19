from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'category', 'posted_by', 'created_at']