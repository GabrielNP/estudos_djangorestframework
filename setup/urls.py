from django.contrib import admin
from django.urls import path

from school.views import students

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('studends/', students)

]
