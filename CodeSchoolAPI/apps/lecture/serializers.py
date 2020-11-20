from rest_framework import serializers

from .models import Lecture, Subscription


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'lecturer_name',
                  'date', 'duration', 'slides_url', 'is_required', 'subscriber', 'admin_user')
        ordering = ['-id']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'user', 'lecture', 'rating', 'reacted_at',)
        orering = ['-id']