from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_class_teacher', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('LMS Info', {'fields': ('role', 'is_class_teacher')}),
    )