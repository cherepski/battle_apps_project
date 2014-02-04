from django.contrib import admin
from member.models import Profile, Avatar

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'created', 'modified')
    list_filter = ('gender', 'created', 'modified')
    search_fields = ['user__username']

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('status',)
    list_filter = ('status',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Avatar, AvatarAdmin)