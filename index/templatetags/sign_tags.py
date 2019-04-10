from django import template
from django.urls import reverse
from django.shortcuts import redirect
from index.models import Signature
from index import urls

register = template.Library()


@register.simple_tag
def add_signature(petition, user):
    # petition = Petition.objects.get(pk=pk)
    # user = User.objects.get(pk=pk_user)

    new_signature = Signature(signer=user)
    new_signature.save()
    petition.signatures.add(new_signature)
    petition.save()

    return reverse("petition-detail", kwargs={"pk": str(petition.pk)})


@register.simple_tag
def user_signed(petition, user):
    if petition.signatures.filter(signer=user).exists():
        return True

    return False
