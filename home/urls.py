from django.urls import path

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:n>', views.detail, name='detail'),
    path('home/<str:nombre>', views.nombre, name='nombre'),
]