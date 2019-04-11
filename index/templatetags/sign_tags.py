from django import template

register = template.Library()


@register.simple_tag
def user_signed(petition, user):
    if petition.signatures.filter(signer=user).exists():
        return True

    return False
