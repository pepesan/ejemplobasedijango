from django.conf.urls import url
from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'REST-EXAMPLE API'
API_DESCRIPTION = 'Un api de pruebas de snippets'
schema_view = get_schema_view(title=API_TITLE)
urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view(),name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(),name="snippet-detail"),
    url(r'^snippets/schema/$', schema_view),
    url(r'^snippets/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),


]

urlpatterns = format_suffix_patterns(urlpatterns)