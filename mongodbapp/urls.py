from django.urls import path

from mongodbapp.views import *


urlpatterns = [
    path('tool', list_view, name='tool-list'),
    path('tool/create', tool_create, name='tool-create'),
    path('tool/<slug:pk>', detail_view, name='tool-detail'),
    path('tool/edit/<slug:pk>', edit_view, name='tool-update-form'),
    path('tool/delete/<slug:pk>', delete_view, name='tool-delete'),
]