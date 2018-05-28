from django.urls import path

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:n>', views.detail, name='detail'),
    path('home/json', views.devuelveJson, name='devuelvejson'),
    path('home/sendjson', views.SendJson, name='sendjson'),
    path('home/sendForm', views.sendForm, name='sendform'),
    path('home/<str:nombre>', views.nombre, name='nombre'),
]