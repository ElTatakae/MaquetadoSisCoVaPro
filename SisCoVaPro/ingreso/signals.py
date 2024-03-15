from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile 

@receiver(post_save, sender=Profile)
def add_user_to_lideres_group(sender, instance, created, **kwargs):
    if created:
        try:
            lideres = Group.objects.get(name='lider')
        except Group.DoesNotExist:
            lideres = Group.objects.create(name='lider')
        instance.user.groups.add(lideres)