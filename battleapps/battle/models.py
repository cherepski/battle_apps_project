import random
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from core.models import TimeStampedModel

STATUS_CHOICES = (('pending', 'pending'), ('allow', 'allow'))

class Battle(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True)
    image = models.ImageField(upload_to="battle/%Y/%m/%d")
    wins = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=100)
    site = models.ForeignKey(Site)

    @property
    def win_percentage(self):
        if not vote:
            return 0
        return 100 * float(win)/float(vote)

    @classmethod
    def battle(cls):
        last = cls.objects.count() - 1
        index1 = random.randint(0, last)
        index2 = random.randint(0, last - 1)
        if index2 == index1: index2 = last

        battle_left = cls.objects.all()[index1]
        battle_right = cls.objects.all()[index2]

        return {"battle_left": battle_left, "battle_right": battle_right}
    
    def __unicode__(self):
        return self.user.username