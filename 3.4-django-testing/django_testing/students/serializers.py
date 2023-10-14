from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django_testing.settings import MAX_STUDENTS_FOR_COURSE

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

