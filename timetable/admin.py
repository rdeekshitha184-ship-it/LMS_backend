from django.contrib import admin
from .models import TimetableEntry

@admin.register(TimetableEntry)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('day', 'period', 'subject', 'teacher_name', 'start_time', 'end_time')
    list_filter = ('day',)