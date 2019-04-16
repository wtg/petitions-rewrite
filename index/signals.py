from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Petition, Signature

@receiver(post_save, sender=Petition)
def petition_created(sender, instance, **kwargs):
    instance.signatures.add(instance.author)
    