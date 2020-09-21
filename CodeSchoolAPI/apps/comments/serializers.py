from rest_framework import serializers

from .models import Comment, CommentRelationship


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = ('lecture', 'comment', 'owner', 'is_liked', 'created_at', )

class CommentRelationshipSerializer(serializers.ModelSerializer):
    model = CommentRelationship
    fields = ('user', 'comment', 'like', 'liked_at', )
