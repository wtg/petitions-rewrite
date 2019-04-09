from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def get_sign_url(petition, user):
    return reverse("sign", kwargs={"pk": str(petition.ID), "pk_user": str(user.pk)})


@register.simple_tag
def user_signed(petition, user):
    if petition.signatures.filter(signer=user).exists():
        return True

    return False
