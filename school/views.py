from rest_framework import viewsets

from school.models import Course, Student
from serializer import CourseSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """List all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """List all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer