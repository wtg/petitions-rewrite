from django.contrib import admin
from .models import Tag, Petition, Response

# add this back in if you want to be able to create tags
"""
class TagAdmin(admin.ModelAdmin):
    pass
"""


class ResponseInline(admin.StackedInline):
    model = Response


class PetitionAdmin(admin.ModelAdmin):
    list_display = ("title", "curr_num_sigs", "has_resp")
    list_filter = ("tags",)
    search_fields = ["title"]
    readonly_fields = ("created_date", "author")  # not editable

    fields = [
        "title",
        "description",
        ("archived", "hidden"),
        "created_date",
        "expected_sig",
        "author",
        "tags",
        "signatures",
    ]

    inlines = [ResponseInline]

    def curr_num_sigs(self, obj):
        return obj.signatures.count()

    def has_resp(self, obj):
        if hasattr(obj, "responses"):
            return "Yes"
        else:
            return "No"

    curr_num_sigs.short_description = "Number of Signatures"
    has_resp.short_description = "Response"

    # gets rid of delete action on petitions list view
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    # can't delete petition in detailed view
    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(Tag, TagAdmin)
admin.site.register(Petition, PetitionAdmin)
