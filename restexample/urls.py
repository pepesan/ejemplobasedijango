from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', snippet_list, name="snippet-list"),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail,name="snippet-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)