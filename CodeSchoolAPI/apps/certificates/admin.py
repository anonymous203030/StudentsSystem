from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    list_filter = ('name','description', 'created_at',)
    filter_horizontal = ()
    ordering = ('created_at',)
    search_fields = ('name','description')


admin.site.register(Certificate, CertificateAdmin)