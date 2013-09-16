from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel

GENDER_CHOICES = (('male', 'male'), ('female', 'female'))
STATUS_CHOICES = (('pending', 'pending'), ('allow', 'allow'))

class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    avatar_status = models.CharField(choices=STATUS_CHOICES, default='allow', max_length=100)
