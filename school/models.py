from django.db import models


class Course(models.Model):
    LEVEL = (
        ('B', 'Baisc'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    course_code = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description

class Student(models.Model):
    name = models.CharField(max_length=30)
    regional_document = models.CharField(max_length=9)
    registry_identification = models.CharField(max_length=11)
    born_at = models.DateField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    PERIOD = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')