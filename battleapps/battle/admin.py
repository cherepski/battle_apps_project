from django.contrib import admin
from battle.models import Battle

class BattleAdmin(admin.ModelAdmin):
    list_display = ('user', 'site', 'created', 'status')
    list_filter = ('site', 'created', 'status')
    search_fields = ['user__username']

admin.site.register(Battle, BattleAdmin)
