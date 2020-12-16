from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views import CourseViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, basename='Courses')
router.register('students', StudentViewSet, basename='Students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
