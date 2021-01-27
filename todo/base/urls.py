from django.urls import path
from .views import *

urlpatterns = [
    path('new/', add,name="new"),
    path('',viewtasks,name='viewtasks'),
]
