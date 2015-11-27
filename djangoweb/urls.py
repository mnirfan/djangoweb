from django.conf.urls import include, url, patterns
from django.contrib import admin
from djangoweb.views import hello, home_page, current_datetime, hours_ahead

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', home_page),
                       url(r'^time/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
                       url(r'^admin/', include(admin.site.urls)),
)