from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views import CourseViewSet, ListRegisteredStudentViewSet, ListRegistrationStudentViewSet, RegistrationViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')
router.register('students', StudentViewSet, basename='Students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('course/<int:pk>/registrations/', ListRegisteredStudentViewSet.as_view()),
    path('student/<int:pk>/registrations/', ListRegistrationStudentViewSet.as_view())
]
