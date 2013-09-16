from django.conf.urls import patterns, include, url

urlpatterns = patterns('battle.views',
    url(r'^$', 'home', name='home'),
)
