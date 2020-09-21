from django.contrib import admin

from .models import Comment, CommentRelationship


class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'lecture', 'created_at', )
    list_filter = ('created_at', )
    ordering = ('created_at', )
    search_fields = ('owner', 'lecture', )

class CommentRelationshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'like', )
    list_filter = ('liked_at', )
    ordering = ('liked_at', )



admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentRelationship, CommentRelationshipAdmin)