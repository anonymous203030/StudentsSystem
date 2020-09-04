from django.contrib import admin

from .models import WaitlistEntry

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'updated_at',)
    search_fields = ('first_name', 'last_name',)
    ordering = ('updated_at',)
    filter_horizontal = ()

admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
