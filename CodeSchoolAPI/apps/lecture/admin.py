from django.contrib import admin

from .models import Lecture, Subscription


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date')
    search_fields = ('title', 'description', 'lecturer_name')
    ordering = ('date',)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'lecture', 'rating', 'reacted_at')
    search_fields = ('user', 'lecture')
    ordering = ('reacted_at', )

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subscription, SubscriptionAdmin)