from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, patterns
from .views import register_by_access_token
 
 
urlpatterns = patterns(
    '',
    url(r'^register-by-token/(?P<backend>[^/]+)/$', register_by_access_token, name='register_by_access_token'),
)
