from rest_framework import serializers

from .models import WaitlistEntry


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistEntry
        fields = ['id', 'first_name', 'last_name', 'email', 'level', 'notes',
                  'created_at']
