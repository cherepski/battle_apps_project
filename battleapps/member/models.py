from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from core.models import TimeStampedModel

GENDER_CHOICES = (('male', 'male'), ('female', 'female'))
STATUS_CHOICES = (('pending', 'pending'), ('allow', 'allow'))

DEFAULT_MALE = static('img/male.jpg')
DEFAULT_FEMALE = static('img/female.jpg')
DEFAULT_IMAGES = [DEFAULT_MALE, DEFAULT_FEMALE]

class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    avatar = models.ForeignKey('Avatar', blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)

    def save(self, *args, **kwargs):
        if not self.avatar:
            avatar = Avatar()
            avatar.status = 'allow'
            if self.gender == 'male':
                avatar.image = DEFAULT_MALE
            else:
                avatar.image = DEFAULT_FEMALE
            self.avatar = avatar.save()

        super(Profile, self).save(*args, **kwargs)

class Avatar(TimeStampedModel):
    image = models.ImageField(upload_to="avatar/%Y/%m/%d", blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='allow', max_length=100)

    def save(self, *args, **kwargs):
        if self.image:
            if any(self.image == DEFAULT_IMAGE for DEFAULT_IMAGE in DEFAULT_IMAGES):
                self.status = 'allow'
            else:
                self.status = 'pending'

        super(Avatar, self).save(*args, **kwargs)