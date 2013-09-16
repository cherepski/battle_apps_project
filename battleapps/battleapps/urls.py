from django.conf.urls import patterns, include, url
from tastypie.api import Api
from member.api.resources import ProfileResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(ProfileResource())
v1_api.register(UserResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'battleapps.views.home', name='home'),
    # url(r'^battleapps/', include('battleapps.foo.urls')),

    # Tastypie API
    #(r'^member/', include('member.urls')),
    url(r'^$', include('battle.urls')),
    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
