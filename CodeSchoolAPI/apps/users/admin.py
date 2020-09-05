from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from .models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'is_staff', 'is_admin', 'is_active', 'is_student')
    list_filter = ('is_admin','is_student', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_student')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',) # searching by email
    ordering = ('id',) # making order by email
    filter_horizontal = ()

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','preferred_name','current_level')
    list_filter = ('user',)

    search_fields = ('user','last_name' 'first_name', 'preferred_name','phone',)
    ordering = ('user',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin) # Registering User And Adding
        # filtering fields for User In UserAdmin
admin.site.register(UserProfile, UserProfileAdmin) # ^