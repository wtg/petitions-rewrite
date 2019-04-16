from django.contrib import admin
from .models import Tag, Petition


class TagAdmin(admin.ModelAdmin):
    pass


class PetitionAdmin(admin.ModelAdmin):
    exclude = ("created_date", "signatures")


admin.site.register(Tag, TagAdmin)
admin.site.register(Petition, PetitionAdmin)
