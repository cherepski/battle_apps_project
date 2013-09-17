from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from member.models import Profile

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'last_login']
        allowed_methods = ['get']

class ProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Profile.objects.all()[:100]
        allowed_methods = ['get']
        resource_name = 'profile'
