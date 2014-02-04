from django.shortcuts import render
from django.views.generic.base import View
from battle.models import Battle

class Index(View):
    def get(self, request):
        battle = Battle.battle()
        return render(request, 'home.html', battle)
