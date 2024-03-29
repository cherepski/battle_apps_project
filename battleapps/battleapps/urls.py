from django.conf.urls import patterns, include, url
from tastypie.api import Api
from battle.api.resources import BattleResource

v1_api = Api(api_name='v1')
v1_api.register(BattleResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Tastypie API
    url(r'^$', include('battle.urls')),
    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
