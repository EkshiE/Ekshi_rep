from django.urls import path

from .views import main
from .views import homework
from .views import group
from .views import timetable

urlpatterns = [
    path('', main, name='main'),
    path('homework/', homework, name='homework'),
    path('group/', group, name='group'),
    path('timetable/', timetable, name='timetable'),
]
