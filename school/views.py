from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Course, Registration, Student
from school.serializer import CourseSerializer, ListRegisteredStudentSerializer, ListRegistrationStudentSerializer, RegistrationSerializer, StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """List all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    """List all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListRegisteredStudentViewSet(generics.ListAPIView):
    """List student registered in a course"""
    serializer_class = ListRegisteredStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset

class ListRegistrationStudentViewSet(generics.ListAPIView):
    """List all student's registration"""
    serializer_class = ListRegistrationStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset

class StudentViewSet(viewsets.ModelViewSet):
    """List all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]