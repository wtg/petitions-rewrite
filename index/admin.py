from django.contrib import admin
from .models import Tag, Petition, Signature, Response


class TagAdmin(admin.ModelAdmin):
    pass

class SignatureAdmin(admin.ModelAdmin):
    pass

'''
class ResponseInline(admin.TabularInline):
    model = Response
'''

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'curr_num_sigs', 'has_resp')
    #inlines = [ResponseInline]


    def curr_num_sigs(self, obj):
        return obj.signatures.count()

    def has_resp(self, obj):
        if obj.senate_response == None:
            return "No"
        else:
            return "Yes"

    curr_num_sigs.short_description = "Number of Signatures"
    has_resp.short_description = "Response"

admin.site.register(Tag, TagAdmin)
admin.site.register(Petition, PetitionAdmin)
admin.site.register(Signature, SignatureAdmin)
