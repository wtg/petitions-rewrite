from django.contrib import admin

from .models import Petition, Tag, Response, User, Signature

admin.site.register(Petition)
admin.site.register(Tag)
admin.site.register(Response)
admin.site.register(User)
admin.site.register(Signature)