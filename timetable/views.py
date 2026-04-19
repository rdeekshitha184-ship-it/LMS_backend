from rest_framework import viewsets, permissions
from accounts.permissions import IsClassTeacher
from .models import TimetableEntry
from .serializers import TimetableSerializer

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = TimetableEntry.objects.all()
    serializer_class = TimetableSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsClassTeacher()]   # Only class teacher can edit
        return [permissions.IsAuthenticated()]