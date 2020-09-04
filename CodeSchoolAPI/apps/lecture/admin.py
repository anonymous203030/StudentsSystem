from django.contrib import admin

from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date')
    search_fields = ('title', 'description', 'lecturer_name')
    ordering = ('date',)



admin.site.register(Lecture, LectureAdmin)