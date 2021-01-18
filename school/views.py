from rest_framework import viewsets

from school.models import Course, Registration, Student
from school.serializer import CourseSerializer, RegistrationSerializer, StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """List all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    """List all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """List all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer