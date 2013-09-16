from django.contrib import admin
from member.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'modified', 'avatar_status')
    list_filter = ('created', 'modified', 'avatar_status')
    search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)
