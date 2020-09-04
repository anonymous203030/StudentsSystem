from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('name','description', 'created_at', 'updated_at')
    # filter_horizontal = ()
    # ordering = ['updated_at']
admin.site.register(Certificate, CertificateAdmin)