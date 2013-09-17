from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from core.models import TimeStampedModel

GENDER_CHOICES = (('male', 'male'), ('female', 'female'))
STATUS_CHOICES = (('pending', 'pending'), ('allow', 'allow'))

DEFAULT_MALE = static('img/male.jpg')
DEFAULT_FEMALE = static('img/female.jpg')

class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    avatar_status = models.CharField(choices=STATUS_CHOICES, default='allow', max_length=100)

    def save(self, *args, **kwargs):
        if self.avatar:
            if self.avatar != DEFAULT_MALE and self.avatar != DEFAULT_FEMALE:
                self.avatar_status = 'pending'
            else:
                self.avatar_status = 'allow'
        else:
            self.avatar_status = 'allow'
            if self.gender == 'male':
                self.avatar = DEFAULT_MALE
            else:
                self.avatar = DEFAULT_FEMALE

        super(Profile, self).save(*args, **kwargs)
