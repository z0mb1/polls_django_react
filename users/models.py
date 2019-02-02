from django.db import models
from django.contrib.auth.models import User
from poll.models import Poll 
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    finished_polls = models.ManyToManyField(Poll, blank=True)
    
    class Meta:
        verbose_name = ('profile')
        verbose_name_plural = ('profiles')

    def __str__(self):
        return '{}-profile'.format(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
