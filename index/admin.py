from django.contrib import admin
from index.models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)