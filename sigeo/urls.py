from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sigeo/', include('sigeo.foo.urls')),

    # Uncomment this for admin:
     (r'^obcine/', include('sigeo.obcine.urls')),
     (r'^admin/', include(admin.site.urls)),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
)

