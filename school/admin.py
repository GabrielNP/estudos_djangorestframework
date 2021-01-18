from django.contrib import admin

from school.models import Course, Registration, Student


class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description',)
    list_display_links = ('id', 'course_code',)
    search_fields = ('course_code',)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period',)
    list_display_links = ('id',)

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'regional_document', 'registry_identification', 'born_at',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Course, Courses)
admin.site.register(Registration, Registrations)
admin.site.register(Student, Students)
