# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'role', 'is_class_teacher']

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role', 'is_class_teacher']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email', ''),
#             password=validated_data['password'],
#             role=validated_data['role'],
#             is_class_teacher=validated_data.get('is_class_teacher', False)
#         )
#         return user

from rest_framework import serializers
from .models import User

STUDENT_CODE = "CLASS2024"
TEACHER_CODE = "TEACH2024"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'role', 'is_class_teacher']

class RegisterSerializer(serializers.ModelSerializer):
    password   = serializers.CharField(write_only=True)
    class_code = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password', 'class_code']

    def validate_class_code(self, value):
        if value != STUDENT_CODE and value != TEACHER_CODE:
            raise serializers.ValidationError(
                "Invalid class code. Please contact your teacher."
            )
        return value

    def create(self, validated_data):
        class_code = validated_data.pop('class_code')

        if class_code == TEACHER_CODE:
            role             = 'teacher'
            is_class_teacher = False
        else:
            role             = 'student'
            is_class_teacher = False

        user = User.objects.create_user(
            username         = validated_data['username'],
            email            = validated_data.get('email', ''),
            password         = validated_data['password'],
            role             = role,
            is_class_teacher = is_class_teacher
        )
        return user