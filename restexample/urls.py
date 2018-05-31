from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^snippets/$', snippet_list, name="snippet-list"),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail,name="snippet-detail"),
]