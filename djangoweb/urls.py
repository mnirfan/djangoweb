from django.conf.urls import include, url, patterns

from djangoweb.views import hello, home_page, current_datetime, hours_ahead


urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', home_page),
                       url(r'^time/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead)
)
