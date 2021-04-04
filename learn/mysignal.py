from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from learn.models import profile

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kw):
    if created:
        profile.objects.create(user=instance,name=instance.username)

     


