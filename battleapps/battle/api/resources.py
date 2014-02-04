from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from battle.models import Battle

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class BattleResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    
    class Meta:
        queryset = Battle.objects.all()
        resource_name = 'battle'