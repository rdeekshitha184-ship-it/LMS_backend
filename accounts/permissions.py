from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    """Only teachers can access this."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsStudent(BasePermission):
    """Only students can access this."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

class IsClassTeacher(BasePermission):
    """Only the class teacher can access this."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_class_teacher