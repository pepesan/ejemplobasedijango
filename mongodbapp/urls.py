from django.urls import path

from mongodbapp.views import *


urlpatterns = [
    path('', ToolListView.as_view(), name='tool-list'),
]