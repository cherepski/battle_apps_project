from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from core.models import TimeStampedModel

STATUS_CHOICES = (('pending', 'pending'), ('allow', 'allow'))

class BattleImage(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True)
    image = models.ImageField(upload_to="battle_images/%Y/%m/%d")
    wins = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=100)
    site = models.ForeignKey(Site)

    @property
    def win_percentage(self):
        if self.votes <= 10:
            return "Minimum votes not reached"

        try:
            return 100 * float(win)/float(vote)
        except ZeroDivisionError:
            return "Minimum votes not reached"

    def __unicode__(self):
        return self.user.username
