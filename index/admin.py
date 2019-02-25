from django.contrib import admin
from .models import Tag, Petition


class TagAdmin(admin.ModelAdmin):
    pass


class PetitionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Petition, PetitionAdmin)
