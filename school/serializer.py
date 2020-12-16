from rest_framework import serializers

from school.models import Course, Student


class CoruseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coruse
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'